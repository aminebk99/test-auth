from models.user import User
from db import db
from flask import jsonify

def create_user(username, password):
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 409
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
