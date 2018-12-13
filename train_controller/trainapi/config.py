"""Default configuration

Use env var to override
"""
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/trainapi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Pin to control the main relay
power_pin = 16

# Motor-Plate config
motor_hat_address = "0x60"
kato_inside_track = 1
kato_outside_track = 2
lgb = 3
