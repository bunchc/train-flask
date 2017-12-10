from trainapi.extensions import io

class Power():
    """Basic Power Control Module
    """
    powerpin = 24
    io.setmode(io.BCM)
    io.setup(powerpin, io.OUT)
    io.output(powerpin, False)
    powerstatus = io.input(powerpin)

    def __repr__(self):
        return "<Power %s>" % self.powerstatus