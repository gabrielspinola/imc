from flask import Blueprint, jsonify, request
import jwt
from datetime import datetime, timedelta

route_user = Blueprint('route_user', __name__)

@route_user.route('/auth', methods=['POST'])
def authorization_route():
    token = jwt.encode({
        'exp': datetime.utcnow() + timedelta(minutes=10),
        'uid': 12
    }, key='1234', algorithm="HS256")
        
    return jsonify({
        'token': token
    }), 200
