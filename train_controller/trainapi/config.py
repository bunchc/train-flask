"""Default configuration

Use env var to override
"""

FLASK_ENV = development
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/trainapi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Pin to control the main relay
power_pin = 16

# MotorHAT Config
trains = [
    {
        'id': 1,
        'name': 'Silver Streak Zephyr',
        'locomotive': 'EMD E5A',
        'manufacturer': 'Kato',
        'throttle_max': 0.4,
        'address': 0x60
    },
    {
        'id': 2,
        'name': 'BNSF Black #4449',
        'locomotive': 'GS-4',
        'scale': 'N',
        'manufacturer': 'Kato',
        'throttle_max': 0.4,
        'address': 0x60
    },
    {
        'id': 4,
        'name': 'Stainz #1',
        'locomotive': 'Stainz',
        'manufacturer': 'LGB',
        'scale': 'G',
        'throttle_max': 0.7,
        'address': 0x61
    }
]
motor_hat_address = "0x60"
kato_inside_track = 1
kato_outside_track = 2
lgb = 3
