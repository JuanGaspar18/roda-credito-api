from marshmallow import Schema, fields, validate, validates, ValidationError

# Objeto de vehiculo para validacion de datos de entrada en la simulacion de credito
SUPPORTED_VEHICLES = [
    "Bicicleta electrica",
    "Moto electrica"
]

# Clase para validacion de datos de la simulacion de credito
class SimulationSchema(Schema):

    # Campos para validacion de datos de entrada en la simulacion de credito
    vehicle_type = fields.Str(required=True, validate=validate.OneOf(SUPPORTED_VEHICLES, error="El tipo de vehículo ingresado no es válido."))
    vehicle_value = fields.Float(required=True, validate=validate.Range(min=500000, error="El valor del vehículo debe ser al menos 500,000 COP."))
    down_payment = fields.Float(required=True, validate=validate.Range(min=0, error="El pago inicial no puede ser negativo."))
    installments = fields.Int(required=True, validate=validate.Range(min=6, max=72, error="El número de cuotas debe estar entre 6 y 72."))

    @validates('down_payment')
    def validate_down_payment(self, value, **kwargs):

        vehicle_value = self.context.get('vehicle_value')

        if 'vehicle_value' is not None and value > vehicle_value:
            raise ValidationError('El pago inicial debe ser menor que el valor del vehículo.')
        
# Clase para validacion de datos de la solicitud de credito
class CreditRequestSchema(Schema):

    # Campos para validacion de datos de entrada en la solicitud de credito
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=100, error="El nombre supera el limite de caracteres."))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=100, error="El apellido supera el limite de caracteres."))
    email = fields.Email(required=True, error_messages={"required": "El correo electrónico es obligatorio."})
    phone = fields.Str(required=True, validate=validate.Regexp(r"^[0-9]+$", error="El número de teléfono no es válido."))
    city = fields.Str(required=True, validate=validate.Length(min=2, max=100, error="La ciudad supera el limite de caracteres."))