# -*- coding: utf-8 -*-

"""
    trainapi.api.train
    ~~~~~~~~~~~~~~~~~~

    API functions to control DC Locomotives via the Adafruit MotorHAT

    :license: BSD, see LICENSE for more details.

"""

from flask_restful_swagger_2 import swagger, Resource
from flask import request

import trainapi.config as cfg
import trainapi.commons.locomotive as display
import trainapi.commons.exceptions as e

from trainapi.models import TrainModel, TrainError
from trainapi.commons.pagination import paginate

class TrainStatus(Resource):
    @swagger.doc({
        'tags': ['status'],
        'description': 'Returns the status of a locomotive',
        'parameters': [
            {
                'name': 'locomotive_id',
                'description': 'Specifies which locomotive between 1 and 4',
                'in': 'path',
                'type': 'integer'
            }
        ],
        'responses': {
            '200': {
                'description': 'Locomotive Status',
                'schema': TrainModel,
                'examples': {
                    'application/json': {
                        'id': 1,
                        'status': 'on',
                        'speed': 175,
                        'direction': 'forward'
                    }
                }
            }
        }
    })
    def get(self, locomotive_id):
        train = display.trainStatus(locomotive_id)
        return TrainModel(**train), 200

class TrainControl(Resource):
    @swagger.doc({
        'tags': ['locomotive', 'control'],
        'description': 'Functions to pilot locomotives',
        'parameters': [
            {
                'name': 'locomotive_id',
                'description': 'Specifies which locomotive between 1 and 4',
                'in': 'path',
                'type': 'integer'
            },
            {
                'name': 'Action',
                'description': 'startTrain, stopTrain, startAllTrains, stopAllTrains, haltTrains, accelerate, decelerate',
                'in': 'path',
                'type': 'string',
            },
            {
                'name': 'direction',
                'description': 'Sets the direction of the train forward or backward',
                'in': 'path',
                'type': 'string'
            },
            {
                'name': 'speed',
                'description': 'Sets the speed of the locomotive between 0 and 10',
                'in': 'path',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Success',
                'schema': TrainModel,
                'examples': {
                    'application/json': {
                        'id': 1,
                        'status': 'on',
                        'speed': 175,
                        'direction': 'forward'
                    }
                }
            },
            '416': {
                'description': 'Request out of range',
                'schema': TrainError,
                'examples': {
                    'application/json': {
                        'errorId': 2,
                        'errorName': 'Speed out of range',
                        'errorDescription': 'The requested speed is invalid. Must request a speed between 0 and 10'
                    }
                }
            }
        }
    })
    def post(self):
        if not request.is_json:
            return TrainError(**e.error[3]), e.error[3]['response']
        
        locomotive_id = request.json.get('locomotive_id', None)
        action = request.json.get('action', None)
        direction = request.json.get('direction', 'forward')
        speed = request.json.get('speed', 7.5)

        if (not action in dir(display)):
            return TrainError(**e.error[5]), e.error[5]['response']
        elif action == "haltTrains":
            trains = display.haltTrains()
            return map(lambda train: TrainModel(**train), trains), 200
        elif action == "stopAllTrains":
            trains = display.stopAllTrains()
            return map(lambda train: TrainModel(**train), trains), 200
        elif action == "startAllTrains":
            if not speed or not direction:
                return TrainError(**e.error[6]), e.error[6]['response']
            else:
                trains = display.startAllTrains(direction, speed)
            return map(lambda train: TrainModel(**train), trains), 200
        else:
            if (not locomotive_id):
                return TrainError(**e.error[4]), e.error[4]['response']
            else:
                if action == "startTrain":
                    if not speed or not direction:
                        return TrainError(**e.error[6]), e.error[6]['response']
                    else:
                        train = display.startTrain(locomotive_id, direction, speed)
                        return TrainModel(**train), 200
                elif action == "stopTrain":
                    train = display.stopTrain(locomotive_id)
                    return TrainModel(**train), 200
                elif action == "accelerate":
                    if not speed:
                        return TrainError(**e.error[6]), e.error[6]['response']
                    else:
                        train = display.accelerate(locomotive_id, speed)
                        return TrainModel(**train), 200
                elif action == "decelerate":
                    if not speed:
                        return TrainError(**e.error[6]), e.error[6]['response']
                    else:
                        train = display.decelerate(locomotive_id, speed)
                        return TrainModel(**train), 200
            