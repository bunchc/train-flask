from trainapi.extensions import io

class Power():
    """Basic Power Control Module
    """
    powerpin = 24
    io.setmode(io.BCM)
    io.setup(powerpin, io.OUT)
    io.output(powerpin, False)


    def __repr__(self):
        powerstatus = io.input(powerpin)
        return "<Power %s>" % powerstatus