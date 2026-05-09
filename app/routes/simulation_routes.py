from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.credit_schema import SimulationSchema
from app.services.simulation_service import SimulationService

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route("/calculate", methods=["POST"])
def calculate_credit():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Se requiere contenido"
            }), 400

        schema = SimulationSchema()

        validated_data = schema.load(data)

        simulation_result = SimulationService.simulate_credit(
            vehicle_type=validated_data["vehicle_type"],
            vehicle_value=validated_data["vehicle_value"],
            down_payment=validated_data["down_payment"],
            installments=validated_data["installments"]
        )

        return jsonify({
            "message": "Simulación de crédito calculada exitosamente",
            "data": simulation_result
        }), 200

    except ValidationError as err:
        return jsonify({
            "error": err.messages
        }), 400

    except ValueError as err:
        return jsonify({
            "error": str(err)
        }), 400

    except Exception as err:
        return jsonify({
            "error": "Ocurrió un error inesperado: " + str(err)
        }), 500