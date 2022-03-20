from flask import request

from functools import wraps

from app.models.auth import User


def auth(func):
    """Authentication jwt middleware decorator/ token checker"""


    @wraps(func)
    def wrapped(*args, **kwargs):
        from heplers.token.token import Token

        # Get Authorization header
        request_token = request.headers.get('Authorization')

        # If header doesn't exists 
        if not request_token:
            return {'message': 'Authorization token is missing'}, 400
        
        # If token valid, continue else throw exception
        try:
            # Get the token, from the Authorization header and decode it
            request_token = request_token.split(" ")[1]
            data = Token.get_data(request_token)

            # Check if user exists with hased username
            user = User.object(username=data).first()
            return {'user': "asd"}
            if user:
                return func(*args,**kwargs, user=user)
            else:
                return {'message':'You are not authorized'}, 400
        except Exception as e:
            print(e.__class__)
            return {'message': 'Invalid token provided'}, 400
        
    return wrapped
