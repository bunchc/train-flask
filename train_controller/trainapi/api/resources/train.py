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

            action = request.json.get('action', None)
            train = request.json.get('train', None)
            direction = request.json.get('direction', 'cw')
            speed = request.json.get('speed', 50)

            if action == "start":
                if not train or not speed or not direction:
                    return jsonify({"msg": "Required parameters missing"}), 400
                else:
                    motor.dcCONFIG(motorplate, train, direction, speed, 5)
                    motor.dcSTART(motorplate, trian)
                    return jsonify({"train": train, "status": "Started"})
            elif action == "stop":
                if not train:
                    return jsonify({"msg": "Missing train in request"}), 400
                else:
                    motor.dcSTOP(motorplate, train)
                    return jsonify({"train": train, "status": "Stopped"})
            elif action == "speed":
                if not train or not speed:
                    return jsonify({"msg": "Required parameters missing"}), 400
                else:
                    motor.dcSPEED(motorplate, train, speed)
                    return jsonify({"train": train, "Speed": speed})
            else:
                return jsonify({"msg": "Invalid action specified", "Action": action})