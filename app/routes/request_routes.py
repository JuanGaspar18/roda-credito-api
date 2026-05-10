from flask import Blueprint, request
from marshmallow import ValidationError

from app.schemas.credit_schema import CreditRequestSchema
from app.schemas.simulation_schema import SimulationInputSchema

from app.services.simulation_service import SimulationService
from app.services.request_service import CreditRequestService
from app.utils.response_handler import (success_response, error_response)


request_bp = Blueprint("request", __name__)

@request_bp.route("", methods=["POST"])
def create_credit_request():

    try:

        if not request.is_json:
            return error_response(
                message="Content-Type must be application/json",
                status_code=400
            )
        
        data = request.get_json()
        if not data:
            return error_response(
                message="No se proporcionaron datos para la solicitud de crédito.",
                status_code=400
            )
        
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

        # Validaciones

        valideted_personal = CreditRequestSchema().load(personal_data)
        validated_simulation = SimulationInputSchema().load(simulation_data)
        
        # Simulacion financiera
        simulation = SimulationService.simulate_credit(
            **validated_simulation
        )

        credit_request = CreditRequestService.create_credit_request(
            valideted_personal,
            simulation
        )

        return success_response(
            data=credit_request.to_dict(),
            message="Solicitud de crédito creada exitosamente",
            status_code=201
        )

    except ValidationError as err:
        return error_response(
            message="Error de validación",
            errors=err.messages,
            status_code=400
        )

    except ValueError as err:
        return error_response(
            message=str(err),
            status_code=400
        )

    except Exception as err:
        return error_response(
            message="Ocurrió un error inesperado",
            errors=str(err),
            status_code=500
        )

@request_bp.route("", methods=["GET"])
def get_all_credit_requests():
    
    try:
        requests = CreditRequestService.get_all_requests()

        return success_response(
            data=[request.to_dict() for request in requests],
            message="Solicitudes de crédito obtenidas exitosamente",
            status_code=200
        )
    
    except Exception as err:
        return error_response(
            message="Ocurrió un error inesperado",
            errors=str(err),
            status_code=500
        )

@request_bp.route("/<int:request_id>", methods=["GET"])
def get_credit_request_by_id(request_id):

    try:
        request_obj = CreditRequestService.get_request_by_id(request_id)

        if not request_obj:
            return error_response(
                message="Solicitud de crédito no encontrada",
                status_code=404
            )

        return success_response(
            data=request_obj.to_dict(),
            message="Solicitud de crédito obtenida exitosamente",
            status_code=200
        )
    
    except Exception as err:
        return error_response(
            message="Ocurrió un error inesperado",
            errors=str(err),
            status_code=500
        )