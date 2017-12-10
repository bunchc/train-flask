from trainapi.extensions import io

class Power():
    """Basic Power Control Module
    """
    powerpin = 24
    io.setmode(io.BCM)
    io.setup(powerpin, io.OUT)
    io.output(powerpin, False)
    powerstatus = 0

    def __repr__(self):
        self.powerstatus = io.input(powerpin)
        return "<Power %s>" % self.powerstatus