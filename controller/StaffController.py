from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import datetime
import os
from auth_middleware import token_required_admin
from models.Staff import Staff
from database import db


def registerStaff():
    if request.method == 'POST':
        req_body = request.get_json()
        name = req_body.get('name', None)
        email = req_body.get('email', None)
        phone = req_body.get('phone', None)
        address = req_body.get('address', None)
        password = req_body.get('password', None)
        print(name, email, phone, address, password)

        if (None not in (name, email, phone, address, password)):
            print(db.session.query(Staff).filter(Staff.email == email).count())
            if (db.session.query(Staff).filter(Staff.email == email).count() == 0):
                try: 
                    hashed_password = generate_password_hash(password, method='sha256')
                    data = Staff(name=name, email=email, phone=phone, address=address, password=hashed_password)
                    db.session.add(data)
                    print(db.session.commit())
                    db.session.commit()
                    return make_response({'message': 'Admin successfully registered' }, 200)
                except:
                    return make_response({'message': 'Error server' }, 500)
            else:
                return make_response({'message' : 'Error. Email already registered'}, 400)
        else:
            return make_response('every field must be filled', 400) 

@token_required_admin
def getAllStaff(current_user):
    if request.method == 'GET':
        staff = Staff.query.all()
        result = jsonify(data=[i.serialize for i in staff])
        return result

def getByID():
    args = request.args
    id = args.get('id')
    user = Staff.query.filter_by(id=id).first()
    return user

def loginStaff():
    if request.method == 'POST':
        req_body = request.get_json()
        email = req_body.get('email', None)
        password = req_body.get('password', None)

        if None in  (req_body, email, password): 
            return make_response('Every field need to be filled', 400, {'Authentication': 'login required"'})   
        
        user = Staff.query.filter_by(email=email).first()
        if check_password_hash(user.password, password):
            token = jwt.encode({'user_id' : user.id, 'admin': 1, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, os.getenv('AUTH_TOKEN_SECRET'), "HS256")
        
            return make_response({'message': 'Admin successfully logged in', 'token': token }, 200)
        
        return make_response('could not verify',  401, {'Authentication': '"login required"'})