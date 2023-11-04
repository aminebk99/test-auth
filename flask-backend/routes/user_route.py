from flask import Flask, jsonify, request, make_response
import jwt
import datetime
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

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        # Generate a JWT token
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

        # Set the token in an HTTP-only cookie
        resp = make_response(jsonify({"message": "Login successful", "token": token}))
        resp.set_cookie('token', token, httponly=True, secure=True)
        return resp

    return 'Login Failed', 401

@app.route('/profile', methods=['GET'])
def get_user_profile():
    token = request.cookies.get('token')

    if token:
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            username = data["username"]

            # Fetch user data from your database
            user = User.query.filter_by(username=username).first()

            if user:
                user_data = {
                    'username': user.username,
                    'email': user.username,  # Replace with actual user data
                    'profile_picture': 'profile.jpg'  # Replace with actual user data
                }
                return jsonify(user_data)

        except jwt.ExpiredSignatureError:
            return 'Token expired', 401

    return 'Token is missing or invalid', 401

