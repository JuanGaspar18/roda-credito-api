from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.config.db import db
from app.models.credit_request import CreditRequest
from app.schemas.credit_schema import CreditRequestSchema
from app.schemas.simulation_schema import SimulationInputSchema
from app.services.simulation_service import SimulationService


request_bp = Blueprint("request", __name__)

@request_bp.route("", methods=["POST"])
def create_credit_request():

    try:

        if not request.is_json:
            return jsonify({
                "success": False,
                "message": "Content-Type must be application/json"
            }), 400
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos para la solicitud de crédito.","success": False,}), 400
        
        personal_data = {
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "city": data.get("city")
        }

        simulation_data = {
            "vehicle_type": data.get("vehicle_type"),
            "vehicle_value": data.get("vehicle_value"),
            "down_payment": data.get("down_payment"),
            "installments": data.get("installments")
        }

        personal_schema = CreditRequestSchema()
        simulation_schema = SimulationInputSchema()
        print(simulation_schema.fields.keys())

        validated_personal = personal_schema.load(personal_data)
        validated_simulation = simulation_schema.load(simulation_data)
        
        # RECALCULAR EN BACKEND
        simulation = SimulationService.simulate_credit(
            **validated_simulation
        )

        # CREAR MODELO CON DATOS YA CONFIABLES
        credit_request = CreditRequest(
            **validated_personal,
            **simulation
        )

        # 4. GUARDAR EN DB
        db.session.add(credit_request)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Solicitud de crédito creada exitosamente",
            "data": credit_request.to_dict()
        }), 201
    except ValidationError as err:
        return jsonify({
            "success": False,
            "message": "Validation error",
            "errors": err.messages
        }), 400
    
    except Exception as err:
        db.session.rollback()
        return jsonify({
            "error": "Ocurrió un error inesperado: ",
            "details": str(err),
            "success": False,
        }),500