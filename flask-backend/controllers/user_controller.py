from services.user_service import create_user
from flask import jsonify

def create_user(data):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Both username and password are required'}), 400
    result = create_user(username=username, password=password)
    return result
