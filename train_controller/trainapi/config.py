"""Default configuration

Use env var to override
"""
DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/trainapi.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Pin to control the main relay
power_pin = 24

# Motor-Plate config
motor_plate_address = 1
lgb = 3
kato = 4