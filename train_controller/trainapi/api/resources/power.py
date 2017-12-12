from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from trainapi.extensions import powerdevice
from trainapi.commons.pagination import paginate


class PowerControl(Resource):
    """Provides power controls
    """
    def get(self, pwr_ctrl):
        pwr_ctrl = pwr_ctrl.lower()
        if pwr_ctrl == "on":
            if powerdevice.value == False:
                powerdevice.on()
                changed = True
                return {"power": powerdevice.value, "changed": changed}
            changed = False
            return {"power": powerdevice.value, "changed": changed}
        elif pwr_ctrl == "off":
            if powerdevice.value == True:
                powerdevice.off()
                changed = True
                return {"power": powerdevice.value, "changed": changed}
            changed = False
            return {"power": powerdevice.value, "changed": changed}
        elif pwr_ctrl == "status":
            return {"power": powerdevice.value}
        else:
            return {"Invalid Reuqest": pwr_ctrl}