from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import user_route

app = Flask(__name__)
CORS(app, supports_credentials=True) 
app.config.from_object('config')  
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app
