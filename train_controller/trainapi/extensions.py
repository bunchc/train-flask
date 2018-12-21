"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
import trainapi.config as cfg

from gpiozero import OutputDevice
from adafruit_motorkit import MotorKit
import flask_restful_swagger_2 as swagger



db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
powerdevice = OutputDevice(cfg.power_pin)
mh = {addr: MotorKit(address=addr) for addr in list(set([ train['address'] for train in cfg.trains ]))}
