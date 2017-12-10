from trainapi.extensions import io

class Power():
    """Basic Power Control Module
    """
    power_pin = 24
    io.setmode(io.BCM)
    io.setup(power_pin, io.OUT)
    io.output(power_pin, False)


    def status(self):
        power_status = io.input(power_pin)
        return power_status
