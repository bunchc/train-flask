from flask import Blueprint
from flask_restful import Api

from trainapi.api.resources import (
    UserResource,
    UserList,
    PowerControl,
    TrainStart,
    TrainStop,
    TrainDirection
)


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(PowerControl, '/power/<pwr_ctrl>')
api.add_resource(TrainStart, '/trian/start')
api.add_resource(TrainStop, '/trian/stop')
api.add_resource(TrainSpeed, '/trian/speed')