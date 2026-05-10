from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.simulation_schema import SimulationInputSchema
from app.services.simulation_service import SimulationService

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route("/calculate", methods=["POST"])
def calculate_credit():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Se requiere contenido",
                "success": False,
            }), 400

        schema = SimulationInputSchema()

        validated_data = schema.load(data)

        simulation_result = SimulationService.simulate_credit(
            vehicle_type=validated_data["vehicle_type"],
            vehicle_value=validated_data["vehicle_value"],
            down_payment=validated_data["down_payment"],
            installments=validated_data["installments"]
        )

        return jsonify({
            "message": "Simulación de crédito calculada exitosamente",
            "data": simulation_result,
            "success": True,
        }), 200

    except ValidationError as err:
        return jsonify({
            "error": err.messages,
            "success": False,
        }), 400

    except ValueError as err:
        return jsonify({
            "error": str(err),
            "success": False,
        }), 400

    except Exception as err:
        return jsonify({
            "error": "Ocurrió un error inesperado: " + str(err),
            "success": False,
        }), 500