from flask import Blueprint
from flask_restful import Api

from trainapi.api.resources import (
    UserResource,
    UserList,
    PowerControl,
    TrainControl,
#    TrainStart,
#    TrainStop,
#    TrainSpeed,
)


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(PowerControl, '/power/<pwr_ctrl>')
api.add_resource(TrainControl, '/train/<train_ctrl>')
#api.add_resource(TrainStart, '/trian/start/<train_ctrl>')
#api.add_resource(TrainStop, '/trian/stop/<train_ctrl>')
#api.add_resource(TrainSpeed, '/trian/speed/<train_ctrl>')