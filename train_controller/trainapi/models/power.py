"""
    trainapi.models.power
    ~~~~~~~~~~~~~~~~~~~~~

    Datamodel for Adafruit Powertail2

    :license: BSD, see LICENSE for more details.

"""

from trainapi.extensions import swagger

class PowerModel(swagger.Schema):
    """Basic Power Control Module
    """
    type = 'object'
    properties = {
        'status': {
            'type': 'boolean'
        }
    }
    required = ['status']
