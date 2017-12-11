from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from trainapi.extensions import powerdevice
from trainapi.commons.pagination import paginate

powerpin = 24

class PowerStatus(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    def get(self):
        return {"power": powerdevice.value}


class PowerOn(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    def get(self):
        return {"power": powerdevice.on()}


class PowerOff(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    def get(self):
        return {"power": powerdevice.off()}