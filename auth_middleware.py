from functools import wraps
import jwt
from flask import request, make_response
from models.Staff import Staff
from models.Customer import Customer
import os

def token_required_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return make_response({
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401)
        try:
            data=jwt.decode(token, os.getenv('AUTH_TOKEN_SECRET'), algorithms=["HS256"])
            current_user = Staff.query.filter_by(id=id)
            if current_user is None or data['admin'] != 1:
                return make_response({
                "message": "Unauthorized User!",
                "data": None,
                "error": "Unauthorized"
            }, 401)
        except Exception as e:
            return make_response({
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500)
        return f(current_user, *args, **kwargs)

    return decorated

def token_required_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return make_response({
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401)
        try:
            data=jwt.decode(token, os.getenv('AUTH_TOKEN_SECRET'), algorithms=["HS256"])
            current_user = Customer.query.filter_by(id=id)
            if current_user is None:
                return make_response({
                "message": "Unauthorized User!",
                "data": None,
                "error": "Unauthorized"
            }, 401)
        except Exception as e:
            return make_response({
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500)
        return f(current_user, *args, **kwargs)

    return decorated