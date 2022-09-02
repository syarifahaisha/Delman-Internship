from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import datetime
import os
from auth_middleware import token_required_user
from models.Customer import Customer
from database import db


def registerCustomer():
    if request.method == 'POST':
        req_body = request.get_json()
        name = req_body.get('name', None)
        email = req_body.get('email', None)
        phone = req_body.get('phone', None)
        address = req_body.get('address', None)
        password = req_body.get('password', None)
        print(name, email, phone, address, password)

        result = {}
        if (None not in (name, email, phone, address, password)):
            print(db.session.query(Customer).filter(Customer.email == email).count())
            if (db.session.query(Customer).filter(Customer.email == email).count() == 0):
                try: 
                    hashed_password = generate_password_hash(password, method='sha256')
                    data = Customer(name=name, email=email, phone=phone, address=address, password=hashed_password)
                    db.session.add(data)
                    db.session.commit()
                    return make_response({'message': 'Customer successfully registered' }, 200)
                except:
                    return make_response({'message': 'Error server' }, 500)
            else:
                return make_response({'message' : 'Error. Email already registered'}, 400)
        else:
            return make_response('every field must be filled', 400) 
        return result

@token_required_user
def getAllCustomer(current_user):
    if request.method == 'GET':
        customer = Customer.query.all()
        result = jsonify(data=[i.serialize for i in customer])
        return result

def loginCustomer():
    if request.method == 'POST':
        req_body = request.get_json()
        email = req_body.get('email', None)
        password = req_body.get('password', None)

        if not req_body or not email or not password: 
            return make_response('could not verify', 400, {'Authentication': 'login required"'})   
        
        user = Customer.query.filter_by(email=email).first()
        if check_password_hash(user.password, password):
            token = jwt.encode({'user_id' : user.id, 'admin': 0, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, os.getenv('AUTH_TOKEN_SECRET'), "HS256")
        
            return make_response({'message': 'User successfully registered', 'token': token }, 200)
        
        return make_response('could not verify',  401, {'Authentication': '"login required"'})