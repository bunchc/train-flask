from flask import request, jsonify
from flask_restful import Resource
from time import sleep

import trainapi.config as cfg
from trainapi.extensions import motor
from trainapi.commons.pagination import paginate

motorplate = cfg.motor_plate_address

def startTrain(self, train, direction, speed):
    """Starts a given train
    """
    if not train or not speed or not direction:
        return jsonify({"msg": "Required parameters missing"}), 400
    motor.dcCONFIG(motorplate, train, direction, speed, 5)
    if motor.dcSTART(motorplate, trian):
        return jsonify({"train": train, "status": "Started"})
    else:
        return jsonify({"msg": "Failed to start train"})


def stopTrain(self, train):
    """Stops a given train
    """
    if not train:
        return jsonify({"msg": "Missing train in request"}), 400
    if motor.dcSTOP(motorplate, train):
        return jsonify({"train": train, "status": "Stopped"})
    else:
        return jsonify({"msg": "Failed to Stop train"})


def trainSpeed(self, train, speed):
    """Chnages the speed of a given train
    """
    if not train or not speed:
        return jsonify({"msg": "Required parameters missing"}), 400

    if motor.dcSPEED(motorplate, train, speed):
        return jsonify({"train": train, "Speed": speed})
    else:
        return jsonify({"msg": "Failed to change speed"})


class TrainControl(Resource):
        """Starts a given train with speed and direction values from config.py
        """
        def get(self):
            return jsonify({"msg": "TrainControl endpoint"})

        def post(self):
            if not request.is_json:
                return jsonify({"msg": "Missing JSON in request"}), 400

            action = request.json.get('action', None)
            train = request.json.get('train', None)
            direction = request.json.get('direction', 'cw')
            speed = request.json.get('speed', 50)

            actions = {
                'start': startTrain(self, train, direction, speed),
                'stop': stopTrain(self, train),
                'speed': trainSpeed(self, train, speed)
            }

            return actions.get(action)