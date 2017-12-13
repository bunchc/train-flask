from flask import request, jsonify
from flask_restful import Resource
from time import sleep

import trainapi.config as cfg
from trainapi.extensions import motor
from trainapi.commons.pagination import paginate


class TrainStart(Resource):
    """Starts a given train with speed and direction values from config.py
    """
    motorplate = cfg.motor_plate_address
    def post(self, train_ctrl):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        train = request.json.get('train', None)
        direction = request.json.get('direction', 'cw')
        speed = request.json.get('speed', 50)

        if not train:
            return jsonify({"msg": "Missing train in request"}), 400

        motor.dcCONFIG(motorplate, train, direction, speed, 5)
        if motor.dcSTART(motorplate, trian):
            return jsonify({"train": train, "status": "Started"})
        else:
            return jsonify({"msg": "Failed to start train"})

class TrainStop(Resource):
    """Stops a given train
    """
    motorplate = cfg.motor_plate_address
    def post(self, train_ctrl):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        train = request.json.get('train', None)

        if not train:
            return jsonify({"msg": "Missing train in request"}), 400

        if motor.dcSTOP(motorplate, train):
            return jsonify({"train": train, "status": "Stopped"})
        else:
            return jsonify({"msg": "Failed to Stop train"})


class TrainSpeed(Resource):
    """Chnages the speed of a given train
    """
    motorplate = cfg.motor_plate_address
    def post(self, train_ctrl):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        train = request.json.get('train', None)
        speed = request.json.get('speed', None)

        if not train or not speed:
            return jsonify({"msg": "Missing train in request"}), 400

        if motor.dcSPEED(motorplate, train, speed):
            return jsonify({"train": train, "Speed": speed})
        else:
            return jsonify({"msg": "Failed to change speed"})
