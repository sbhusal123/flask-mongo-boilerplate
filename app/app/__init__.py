from telnetlib import SE
from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from flask_mongoengine import MongoEngine
from marshmallow import ValidationError

from settings import SWAGGER_SETTINGS, DATABASE, SECRET

import json

app = Flask("app")

# secrets
app.config['SECRET_KEY'] = SECRET

# setup databae
app.config['MONGODB_SETTINGS'] = DATABASE
db = MongoEngine(app)


# update swagger configs
app.config.update(SWAGGER_SETTINGS)
docs = FlaskApiSpec(app)


def register_apis():
    """Register blueprint and swagger docs"""
    from app.api import auth_api
    from app.api.views.auth import AuthToken
    
    app.register_blueprint(auth_api)
    docs.register(AuthToken, blueprint='auth_api')

def register_commands():
    """register custom cli commands"""
    from management import management_command
    app.cli.add_command(management_command)

@app.errorhandler(Exception)
def unexpected_error_handler(error):
    """App wide error handler for uncaught exceptions"""
    print(error.__class__)
    rv = dict({'message': json.dumps("asd")})
    return rv, 400

@app.errorhandler(ValidationError)
def error_handler(error):
    """App wide error handler for validation error"""
    rv = dict({'message': json.dumps(error.messages)})
    return rv, 400

register_apis()
register_commands()
