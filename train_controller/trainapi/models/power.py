import RPi.GPIO as io

class Power(io):
    """Basic Power Control Module
    """

    # Initialize GPIO, and ensure fan is off
    io.setmode(io.BCM)
    io.setup(power_pin, io.OUT)
    io.output(power_pin, False)

    def __init__(self, **kwargs):
        super(Power, self).__init__(**kwargs)

