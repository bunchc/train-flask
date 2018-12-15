"""
    trainapi.models.train
    ~~~~~~~~~~~~~~

    Datamodel for train control

    :license: BSD, see LICENSE for more details.

"""

from trainapi.extensions import ma, swagger, pwd_context

class TrainModel(swagger.Schema):
    """Model containing all current information about a locomotive
    """
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64'
        },
        'status': {
            'type': 'string'
        },
        'direction': {
            'type': 'string'
        },
        'speed': {
            'type': 'integer',
            'format': 'int64'
        }
    }
    required = ['id']

class TrainError(swagger.Schema):
    """Model for reporting locomotive control errors
    """
    type = 'object'
    properties = {
        'errorID': {
            'type': 'integer',
            'format': 'int64'
        },
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        }
    }
    required = ['errorId']
