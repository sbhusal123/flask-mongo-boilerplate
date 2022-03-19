"""
Project wide settings
"""

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

DEBUG = True

"""
Generate using: os.urandom(12).hex()
"""
SECRET = "ede509945c147a831b39f772"


# SWAGGER ui and docs
SWAGGER_SETTINGS = {
    'APISPEC_SPEC': APISpec(
        title='Falsk App',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
}

# database
DATABASE = {
    'db': 'myapp',
    # 'username': '<username>',
    # 'password': '<password>',
    # 'port': '27017',
    # 'host': 'localhost'
}
