from flask import Flask, jsonify, request
from controllers.user_controller import create_user

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    result = create_user(data)
    return result