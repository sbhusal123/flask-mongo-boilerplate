from flask import Flask
from flask_mongoengine import MongoEngine

from flask_apispec.extension import FlaskApiSpec
from common.exception import ApiValidationError

from settings import SWAGGER_SETTINGS, DATABASE, SECRET

from management import management_command

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
    from app.api import AuthToken, AuthUser
    
    app.register_blueprint(auth_api)
    docs.register(AuthToken, blueprint='auth_api')
    docs.register(AuthUser, blueprint='auth_api')

def register_commands():
    """register custom cli commands"""
    app.cli.add_command(management_command)


@app.errorhandler(ApiValidationError)
def unexpected_error_handler(error):
    """App wide error handler for swagger schema exceptions"""
    rv = dict({'message': str(error)})
    return rv, 400


@app.errorhandler(Exception)
def unexpected_error_handler(error):
    """App wide error handler for uncaught exceptions"""
    rv = dict({'message': "Unknown exception occured"})
    return rv, 400

register_apis()
register_commands()
