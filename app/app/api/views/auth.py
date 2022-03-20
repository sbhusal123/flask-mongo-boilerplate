# core flask
from flask import Blueprint
from flask_restful import Api, Resource

# swagger
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

# schemas
from ..schemas.auth import  AuthSchema, AuthTokenResponseSchema, AuthUser
from common.schemas import ErrorResponseSchema

# models
from ...models.auth import User

# middlewares
from app.middlewares.login_required import auth

# utils
from werkzeug.security import check_password_hash
from helpers.token.token import Token



class AuthToken(MethodResource, Resource):

    @doc(description='Get JWT Token', tags=['Authentication'])
    @use_kwargs(AuthSchema, location=('json'))
    @marshal_with(ErrorResponseSchema, code=400)
    @marshal_with(AuthTokenResponseSchema, code=201)
    def post(self, **kwargs):
        user = User.objects(username=kwargs.get('username')).first()

        # check if user exists
        if not user:
            return {"message": "Invalid credentials"}, 400

        if check_password_hash(user["password"], kwargs.get('password')):
            token = Token().get_token(user.username)
            return {"token": token}, 200
        else:
            return {"message": "Invalid credentials"}, 400


class AuthUser(MethodResource, Resource):

    @doc(description='Currently Logged in User', tags=['Authentication'])
    @marshal_with(ErrorResponseSchema, code=400)
    @marshal_with(AuthUser, code=200)
    @auth
    def get(self, user):
        return {"user": user.username}, 200


auth_api = Blueprint('auth_api', __name__)
api = Api(auth_api)

api.add_resource(AuthToken, '/auth')
api.add_resource(AuthUser, '/me')
