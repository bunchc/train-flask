from flask import request, jsonify
from flask_restful import Resource
from time import sleep

from trainapi.extensions import motor
from trainapi.commons.pagination import paginate


class TrainStart(Resource):
    """Starts a given train with speed and direction values from config.py
    """
    motorplate = app.config['MOTOR_PLATE_ADDRESS']
    def post():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        train = request.json.get('train', None)
        direction = request.json.get('direction', 'cw')
        speed = request.json.get('speed', 50)

        if not train:
            return jsonify({"msg": "Missing train in request"}), 400

        if motor.dcSTART(motorplate, app.config[train], direction, speed, 5):
            return jsonify({"train": train, "status": "Started"})
        else:
            return jsonify({"msg": "Failed to start train"})

class TrainStop(Resource):
    """Stops a given train
    """
    motorplate = app.config['MOTOR_PLATE_ADDRESS']
    def post():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        train = request.json.get('train', None)

        if not train:
            return jsonify({"msg": "Missing train in request"}), 400

        if motor.dcSTART(motorplate, app.config[train]):
            return jsonify({"train": train, "status": "Stopped"})
        else:
            return jsonify({"msg": "Failed to Stop train"})


class TrainSpeed(Resource):
    """Chnages the speed of a given train
    """
    motorplate = app.config['MOTOR_PLATE_ADDRESS']
    def post():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        train = request.json.get('train', None)
        speed = request.json.get('speed', None)

        if not train or not speed:
            return jsonify({"msg": "Missing train in request"}), 400

        if motor.dcSSPEED(motorplate, app.config[train], speed):
            return jsonify({"train": train, "Speed": speed})
        else:
            return jsonify({"msg": "Failed to change speed"})
