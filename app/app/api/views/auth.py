# core flask
import json
from flask import Blueprint, jsonify
from flask_restful import Api, Resource

# swagger
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

# schemas
from ..schemas.auth import  AuthSchema, AuthErrorResponseSchema, AuthTokenResponseSchema

# models
from ...models.auth import User

from werkzeug.security import check_password_hash


class AuthToken(MethodResource, Resource):

    @doc(description='Get JWT Token', tags=['Authentication'])
    @use_kwargs(AuthSchema, location=('json'))
    @marshal_with(AuthErrorResponseSchema, code=400)
    @marshal_with(AuthTokenResponseSchema, code=201)
    def post(self, **kwargs):
        print(self.__dict__)
        payload = AuthSchema(kwargs)
        user = User.objects(username=kwargs.get('username')).first()

        # check if user exists
        if not user:
            return {"message": "Invalid credentials"}, 400

        if check_password_hash(user["password"], kwargs.get('password')):
            return {"token": "eye.adlaskdj120391823khasd"}, 200
        else:
            return {"message": "Invalid credentials"}, 400


auth_api = Blueprint('auth_api', __name__)
api = Api(auth_api)

api.add_resource(AuthToken, '/auth')
