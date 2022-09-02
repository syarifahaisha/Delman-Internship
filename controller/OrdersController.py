from flask import request, jsonify, make_response

from models.Orders import Orders

def getAllOrders():
    if request.method == 'GET':
        order = Orders.query.all()
        result = jsonify(data=[i.serialize for i in order])
        return result

