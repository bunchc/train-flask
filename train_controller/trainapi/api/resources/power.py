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
        powerdevice.on()
        return {"power": powerdevice.value}


class PowerOff(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    def get(self):
        powerdevice.off()
        return {"power": powerdevice.value}


class PowerControl(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    def get(self, pwr_ctrl):
        pwr_ctrl = pwr_ctrl.lower()
        if pwr_ctrl == "on":
            if powerdevice.value.lower() == "false":
                powerdevice.on()
                changed = True
                return {"power": powerdevice.value, "changed": changed}
            changed = False
            return {"power": powerdevice.value, "changed": changed}
        elif pwr_ctrl == "off":
            if powerdevice.value.lower() == "true":
                powerdevice.off()
                changed = True
                return {"power": powerdevice.value, "changed": changed}
            changed = False
            return {"power": powerdevice.value, "changed": changed}
        elif pwr_ctrl == "status":
            return {"power": powerdevice.value}
        else:
            return {"Invalid Reuqest": pwr_ctrl}