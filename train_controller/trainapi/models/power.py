from trainapi.extensions import ma,powerdevice


class Power(input):
    """Basic Power Control Module
    """
    def __init__(self, **kwargs):
        super(Power, self).__init__(**kwargs)
        self.powerstatus = powerdevice.value


    def __repr__(self):
        return "<Power %s>" % self.powerstatus
