from flask import request, jsonify
from flask_restful import Resource
from time import sleep

import trainapi.config as cfg
from trainapi.extensions import motor
from trainapi.commons.pagination import paginate

motorplate = cfg.motor_plate_address

class TrainControl(Resource):
        """Starts a given train with speed and direction values from config.py
        """
        def get(self):
            return jsonify({"msg": "TrainControl endpoint"})

        def post(self):
            if not request.is_json:
                return jsonify({"msg": "Missing JSON in request"}), 400

            my_action = request.json.get('action', None)
            my_train = request.json.get('train', None)
            my_direction = request.json.get('direction', 'cw')
            my_speed = request.json.get('speed', 50)

            if my_action == "start":
                if not my_train or not my_speed or not my_direction:
                    return jsonify({"msg": "Required parameters missing"}), 400
                else:
                    motor.dcCONFIG(motorplate, request.json.get('train', None), request.json.get('direction', 'cw'), request.json.get('speed', 50), 5)
                    motor.dcSTART(motorplate, my_train)
                    return jsonify({"train": my_train, "status": "Started"})
            elif my_action == "stop":
                if not my_train:
                    return jsonify({"msg": "Missing train in request"}), 400
                else:
                    motor.dcSTOP(motorplate, my_train)
                    return jsonify({"train": my_train, "status": "Stopped"})
            elif my_action == "speed":
                if not my_train or not my_speed:
                    return jsonify({"msg": "Required parameters missing"}), 400
                else:
                    motor.dcSPEED(motorplate, my_train, my_speed)
                    return jsonify({"train": my_train, "Speed": my_speed})
            else:
                return jsonify({"msg": "Invalid action specified", "Action": my_action})