from settings.config import Config
from flask import Flask, escape, request
from flask_restful import Api


def create_app(config_class=Config):
    """
    A create app method from config file (class).
    
    Attributes:
        :Config: Class whitch contains configuration from .env and all other
    """
    #set configuration to the app
    app = Flask(__name__)
    api = Api(app)

    #simpler way - create Config class
    app.config.from_object(Config)

    #at the end return app
    return app

def app_config(app, var, default):
    """
        Get global app_config
    """
    return app.config.get(var) if app.config.get(var) else default
