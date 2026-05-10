from flask import Blueprint, request
from marshmallow import ValidationError

from app.schemas.simulation_schema import SimulationInputSchema
from app.services.simulation_service import SimulationService

from app.utils.response_handler import (success_response, error_response)

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route("/simulate", methods=["POST"])
def calculate_credit():

    try:

        # Validar content-type
        if not request.is_json:

            return error_response(
                message="Content-Type must be application/json",
                status_code=400
            )

        data = request.get_json()

        # Validar contenido
        if not data:

            return error_response(
                message="Se requiere contenido para realizar la simulación.",
                status_code=400
            )

        # Validar payload
        validated_data = SimulationInputSchema().load(data)

        # Ejecutar simulación
        simulation_result = SimulationService.simulate_credit(
            **validated_data
        )

        return success_response(
            data=simulation_result,
            message="Simulación de crédito calculada exitosamente",
            status_code=200
        )

    except ValidationError as err:

        return error_response(
            message="Validation error",
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
            message="Ocurrió un error inesperado.",
            errors=str(err),
            status_code=500
        )