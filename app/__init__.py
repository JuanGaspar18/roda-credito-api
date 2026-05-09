from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from app.config.db import db

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    CORS(app)
    
    # with app.app_context():
    #     from . import routes
    #     db.create_all()

    return app