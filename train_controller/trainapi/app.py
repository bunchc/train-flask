from flask import Flask

from trainapi import auth, api
from trainapi.extensions import db, jwt


def create_app(config=None, testing=True):
    """Application factory, used to create application
    """
    app = Flask('trainapi')

    configure_app(app)
    configure_extensions(app)
    register_blueprints(app)

    return app


def configure_app(app, testing=True):
    """set configuration for application
    """
    # default configuration
    app.config.from_object('trainapi.config')

    if testing is True:
        # override with testing config
        app.config.from_object('trainapi.configtest')
    else:
        # override with env variable, fail silently if not set
        app.config.from_envvar("TRAINAPI_CONFIG", silent=True)


def configure_extensions(app):
    """configure flask extensions
    """
    db.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
