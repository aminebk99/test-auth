from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import jwt
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.user import User


app = Flask(__name__)
CORS(app, supports_credentials=True) 
app.config.from_object('config')  
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models.user import User




# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')

#     user = User.query.filter_by(username=username, password=password).first()

#     if user:
#         # Generate a JWT token
#         payload = {
#             'username': username,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
#         }
#         token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

#         # Set the token in an HTTP-only cookie
#         resp = make_response(jsonify({"message": "Login successful", "token": token}))
#         resp.set_cookie('token', token, httponly=True, secure=True)
#         return resp

#     return 'Login Failed', 401

# @app.route('/profile', methods=['GET'])
# def get_user_profile():
#     token = request.cookies.get('token')

#     if token:
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#             username = data["username"]

#             # Fetch user data from your database
#             user = User.query.filter_by(username=username).first()

#             if user:
#                 user_data = {
#                     'username': user.username,
#                     'email': user.username,  # Replace with actual user data
#                     'profile_picture': 'profile.jpg'  # Replace with actual user data
#                 }
#                 return jsonify(user_data)

#         except jwt.ExpiredSignatureError:
#             return 'Token expired', 401

#     return 'Token is missing or invalid', 401

if __name__ == '__main__':
    app
