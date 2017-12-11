from flask import Blueprint
from flask_restful import Api

from trainapi.api.resources import UserResource, UserList, PowerStatus, PowerOn, PowerOff


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(PowerStatus, '/power/status')
api.add_resource(PowerOn, '/power/on')
api.add_resource(PowerOff, '/power/off')
