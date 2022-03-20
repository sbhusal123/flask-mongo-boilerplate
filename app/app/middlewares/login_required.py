from flask import request

from app.models.auth import User

from helpers.token import Tokenizer

from functools import wraps


def auth(func):
    """Authentication jwt middleware decorator/ token checker
       returns user object as extra arg to decorated function
    """


    @wraps(func)
    def wrapped(*args, **kwargs):

        # Get Authorization header
        request_token = request.headers.get('Authorization')

        # If header doesn't exists 
        if not request_token:
            return {'message': 'Authorization token is missing'}, 400
        
        # If token valid, continue else throw exception
        try:
            # Get the token, from the Authorization header and decode it
            request_token = request_token.split(" ")[1]


            data = Tokenizer().get_data(str(request_token))
            print(data)
            if not data:
                return {'message':'Invalid token.'}, 400

            # Check if user exists with hased username
            user = User.objects(username=data).first()
            if user:
                return func(*args,**kwargs, user=user)
            else:
                return {'message':'You are not authorized'}, 400
        except Exception as e:
            print(e.__class__)
            return {'message': 'Some exception occured'}, 400
        
    return wrapped
