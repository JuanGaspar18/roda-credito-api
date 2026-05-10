from marshmallow import Schema, fields, validate, validates_schema, ValidationError

# Objeto de vehiculo para validacion de datos de entrada en la simulacion de credito
SUPPORTED_VEHICLES = [
    "Bicicleta eléctrica",
    "Moto eléctrica"
]

# Clase para validacion de datos de la simulacion de credito
class SimulationInputSchema(Schema):

    # Campos para validacion de datos de entrada en la simulacion de credito
    vehicle_type = fields.Str(required=True, validate=validate.OneOf(SUPPORTED_VEHICLES, error="El tipo de vehículo ingresado no es válido."))
    vehicle_value = fields.Float(required=True, validate=validate.Range(min=500000, error="El valor del vehículo debe ser al menos 500,000 COP."))
    down_payment = fields.Float(required=True, validate=validate.Range(min=0, error="El pago inicial no puede ser negativo."))
    installments = fields.Int(required=True, validate=validate.Range(min=6, max=72, error="El número de cuotas debe estar entre 6 y 72."))

    @validates_schema
    def validate_down_payment(self, data, **kwargs):

        vehicle_value = data.get('vehicle_value')
        down_payment = data.get('down_payment')

        if vehicle_value is not None and down_payment is not None and down_payment > vehicle_value:
            raise ValidationError('El pago inicial debe ser menor que el valor del vehículo.')