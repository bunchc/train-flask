"""
    trainapi.models.power
    ~~~~~~~~~~~~~~~~~~~~~

    Datamodel for Adafruit Powertail2

    :license: BSD, see LICENSE for more details.

"""

from trainapi.extensions import ma, swagger, powerdevice

class PowerModel(swagger.Schema):
    """Basic Power Control Module
    """
    type = 'object'
    properties = {
        'status': {
            'type': 'string'
        }
    }
    required = ['powerPin']
    
    def __init__(self, **kwargs):
        super(Power, self).__init__(**kwargs)
        self.powerstatus = powerdevice.value


    def __repr__(self):
        return "<Power %s>" % self.powerstatus
