# -*- coding: utf-8 -*-

"""
    trainapi.api.power
    ~~~~~~~~~~~~~~~~~~

    API functions to control DC Locomotives via the Adafruit MotorHAT

    :license: BSD, see LICENSE for more details.

"""

from flask import request
from flask_restful_swagger_2 import swagger, Resource

from trainapi.extensions import powerdevice
from trainapi.commons.pagination import paginate
from trainapi.models import PowerModel
import trainapi.commons.exceptions as e

class PowerStatus(Resource):
    @swagger.doc({
        'tags': ['power'],
        'description': 'Return the current power state of the display',
        'parameters': [
            {
                'name': 'status',
                'description': 'Returns the current power state of the display',
                'in': 'path',
                'type': 'boolean'
            }
        ],
        'responses': {
            '200': {
                'description': 'Power state of the display',
                'schema': PowerModel,
                'examples': {
                    'application/json': {
                        'status': 'on'
                    }
                }
            }
        }
    })
    def get(self):
        status = {
            'status': powerdevice.value
        }
        
        return PowerModel(**status), 200

class PowerControl(Resource):
    @swagger.doc({
        'tags': ['power'],
        'description': 'Turn the display on or off',
        'parameters': [
            {
                'name': 'status',
                'description': 'Defines if the display should be on or off',
                'in': 'path',
                'type': 'boolean'
            }
        ],
        'responses': {
            '200': {
                'description': 'Power state of the display',
                'schema': PowerModel,
                'examples': {
                    'application/json': {
                        'status': True
                    }
                }
            },
            '400': {
                'description': 'Invalid powerstate requested',
                'schema': PowerModel,
                'examples': {
                    'application/json': {
                        'status': False
                    }
                }
            }
        }
    })
    def post(self):
        powerStatus = request.json.get('status', None)
        if ((powerStatus == "on" and powerdevice.value == True) or (powerStatus == "off" and powerdevice.value == False)):
            status = {
                'status': powerdevice.value
            }
            return PowerModel(**status), 400
        else:
            if (powerStatus == "on"):
                powerdevice.on()
            else:
                powerdevice.off()
            
            status = {
                'status': powerdevice.value
            }
            return PowerModel(**status), 200
