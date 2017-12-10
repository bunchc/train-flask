from trainapi.extensions import io

class Power(io):
    """Basic Power Control Module
    """
    power_pin = 24
    io.setmode(io.BCM)
    io.setup(power_pin, io.OUT)
    io.output(power_pin, False)


#    def __init__(self, **kwargs):
#        super(Power, self).__init__(**kwargs)
#
#
#    def __repr__(self):
#        return "<Power %s>" % self.power_pin


    def status(self):
        power_status = io.input(power_pin)
        return "<Power: %s>" % power_status
