from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from trainapi.models import Power
from trainapi.extensions import ma, db
from trainapi.commons.pagination import paginate


class PowerControl(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    def get(self):
        power_status = Power.powerstatus
        return {"power": power_status}

    def put(self, power_status):
        pass
