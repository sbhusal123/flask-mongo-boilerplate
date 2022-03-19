# core flask
from flask import Blueprint
from flask_restful import Api, Resource

# swagger
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

# schemas
from ..schemas.auth import  AuthSchema


class AuthToken(MethodResource, Resource):

    @doc(description='Get JWT Token', tags=['Authentication'])
    @use_kwargs(AuthSchema, location=('json'))
    @marshal_with(AuthSchema)
    def post(self, **kwargs):
        print(kwargs)
        return {"token": "eye.1ysdalsdkjsad"}


auth_api = Blueprint('auth_api', __name__)
api = Api(auth_api)

api.add_resource(AuthToken, '/auth')
