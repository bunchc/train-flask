# -*- coding: utf-8 -*-

"""
    trainapi.views
    ~~~~~~~~~~~~~~

    This module instantiates the trainapi

    :license: BSD, see LICENSE for more details.

"""

from flask import Blueprint
from flask_restful_swagger_2 import Api

from trainapi.api.resources import (
    UserResource,
    UserList,
    PowerControl,
    TrainControl,
    TrainStatus,
)

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, api_version='1.0', api_spec_url='/api/swagger')

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(PowerControl, '/power/<pwr_ctrl>')
api.add_resource(TrainControl, '/train')
api.add_resource(TrainStatus, '/train/<int:locomotive_id>')
