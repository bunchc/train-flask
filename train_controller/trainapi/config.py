"""Default configuration

Use env var to override
"""

# Driver Configuration
# ~~~~~~~~~~~~~~~~~~~~
#
# Tells the app which driver[s] to use to control your trains.
# The example config below is basic. See the README for a
# specific driver for recommendations and advanced features.

drivers = [
    {
        # Driver for the Adafruit MotorHAT
        # Provides basic control of DC trains
        "driver": "MotorHAT",
        "enabled": True,
        # Optional: If using the Adafruit or similar
        # relay to control power for the display,
        # specify the GPIO pin it is connected to.
        "power_pin": 16
    },
    {
        # Dummy driver
        # A lot of the python modules used in other drivers
        # can only be used on a Raspberry Pi or similar.
        # The dummy driver provides all the same functionality
        # But returns dummy data.
        "driver": "Dummy",
        "enabled": False,
    },
    {
        # DCC Driver
        # TODO: Placeholder for a future DCC driver
        "driver": "DCC",
        "enabled": False
    },
    {
        # TMCC Driver
        # TODO: Placeholder for Lionel TMCC Driver
        "driver": "TMCC",
        "enabled": False,
    }
]

# Train Configuration
# ~~~~~~~~~~~~~~~~~~~
#
# Tells the app about the trains you have and how to control them.

trains = [
    {
        'id': 1,
        'name': 'Silver Streak Zephyr',
        'locomotive': 'EMD E5A',
        'manufacturer': 'Kato',
        'driver_config': {
            'driver': "MotorHAT",
            'address': 0x60,
            'throttle_max': 0.4
        }
    },
    {
        'id': 2,
        'name': 'BNSF Black #4449',
        'locomotive': 'GS-4',
        'scale': 'N',
        'manufacturer': 'Kato',
        'driver_config': {
            'driver': "MotorHAT",
            'address': 0x60,
            'throttle_max': 0.4
        }
    },
    {
        'id': 4,
        'name': 'Stainz #1',
        'locomotive': 'Stainz',
        'manufacturer': 'LGB',
        'scale': 'G',
        'driver_config': {
            'driver': "MotorHAT",
            'address': 0x61,
            'throttle_max': 0.7
        }
    }
]

# Controls how the app itself runs
FLASK_ENV = "development"
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/trainapi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
