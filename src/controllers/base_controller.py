import os
import jwt
import traceback
from functools import wraps
from collections import namedtuple

from flask import request
import flask_restful

from src.utils import flask_http_exceptions


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            UserSession = namedtuple('UserSession', ['email', 'username', 'cognito_id'])

            auth_headers = request.headers.get('Authorization', '').split()
            if len(auth_headers) == 1:
                raise flask_http_exceptions.HTTPTokenRequired
            elif len(auth_headers) != 2:
                raise flask_http_exceptions.HTTPInvalidTokenError

            token = auth_headers[1]
            data = jwt.decode(token, verify=False)
            
            cognito_id = data['sub']
            email = data['email']
            username = data['username']

            current_user = UserSession(
                email=email,
                username=username,
                cognito_id=cognito_id
            )
            return func(current_user, *args, **kwargs)
        except jwt.ExpiredSignatureError as e:
            raise flask_http_exceptions.HTTPExpiredSignatureError
        except jwt.InvalidTokenError as e:
            raise flask_http_exceptions.HTTPInvalidTokenError
        except Exception as e:
            traceback.print_exc()
            raise e
        finally:
            pass
    return wrapper

class BaseController(flask_restful.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__()

    method_decorators = [token_required]