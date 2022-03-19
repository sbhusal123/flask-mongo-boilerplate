from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from flask_mongoengine import MongoEngine

from settings import SWAGGER_SETTINGS, DATABASE

app = Flask("app")

# setup databae
app.config['MONGODB_SETTINGS'] = DATABASE
db = MongoEngine(app)


# update swagger configs
app.config.update(SWAGGER_SETTINGS)
docs = FlaskApiSpec(app)


def register_apis():
    from app.api import auth_api
    from app.api.views.auth import AuthToken
    
    app.register_blueprint(auth_api)
    docs.register(AuthToken, blueprint='auth_api')

register_apis()
