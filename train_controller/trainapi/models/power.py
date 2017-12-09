import RPi.GPIO as io

class Power(io):
    """Basic Power Control Module
    """

    # Define the GPIO pin controlling power relay
    power_pin = 24


    def __init__(self, **kwargs):
        super(Power, self).__init__(**kwargs)
        # Initialize GPIO, and ensure power is off
        io.setmode(io.BCM)
        io.setup(power_pin, io.OUT)
        io.output(power_pin, False)

    def status(self):
        power_status = io.input(power_pin)
        return "<Power: %s>" % power_status
