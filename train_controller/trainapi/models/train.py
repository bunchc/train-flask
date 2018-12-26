"""
    trainapi.models.train
    ~~~~~~~~~~~~~~

    Datamodel for train control

    :license: BSD, see LICENSE for more details.

"""

from trainapi.extensions import swagger

class TrainModel(swagger.Schema):
    """Model containing all current information about a locomotive
    """
    type = 'object'
    properties = {
        'id': {
            'type': 'integer',
            'format': 'int64'
        },
        'name': {
            'type': 'string'
        },
        'locomotive': {
            'type': 'string'
        },
        'manufacturer': {
            'type': 'string'
        },
        'throttle_max': {
            'type': 'number',
            'format': 'float'
        },
        'address': {
            'type': 'string'
        },
        'status': {
            'type': 'string'
        },
        'direction': {
            'type': 'string'
        },
        'speed': {
            'type': 'float'
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
        },
        'response': {
            'type': 'integer',
            'format': 'int64'
        }
    }
    required = ['errorID']
