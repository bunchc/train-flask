from trainapi.extensions import io

class Power():
    """Basic Power Control Module
    """
    powerpin = 24
    io.setmode(io.BCM)
    io.setup(powerpin, io.OUT)
    powerstatus = io.input(powerpin)


    def __init__(self, **kwargs):
        super(Power, self).__init__(**kwargs)
        self.powerstatus = io.input(self.powerpin)


    def __repr__(self):
        return "<Power %s>" % self.powerstatus