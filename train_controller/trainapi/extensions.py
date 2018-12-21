"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
import trainapi.config as cfg
import flask_restful_swagger_2 as swagger

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')

# If the MotorHAT driver is enabled, instansiate an instance of the MotorKit object for each of them
motorhat_enabled = [driver['driver'] for driver in cfg.drivers if driver['driver'].lower() == "motorhat" and driver['enabled'] == True]
if (motorhat_enabled):
    from adafruit_motorkit import MotorKit
    mh = {addr: MotorKit(address=addr) for addr in list(set([ train['driver_config']['address'] for train in cfg.trains ]))}
    # If power_pin is specified, import the GPIO library and configure the power device
    power_pin = [driver['power_pin'] for driver in cfg.drivers if driver['driver'].lower() == "motorhat" and 'power_pin' in driver][0]
    if (power_pin):
        from gpiozero import OutputDevice
        powerdevice = OutputDevice(power_pin)
