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

    CORS(app, resources={
        r"/api/*": {
            "origins": "http://localhost:5173"
        }
    })

    from app.models.credit_request import CreditRequest
    from app.routes.simulation_routes import simulation_bp
    from app.routes.request_routes import request_bp

    app.register_blueprint(simulation_bp, url_prefix='/api/simulations')
    app.register_blueprint(request_bp, url_prefix='/api/requests')

    return app