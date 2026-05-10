from marshmallow import Schema, fields, validate, validates_schema, ValidationError

from app.schemas.simulation_schema import SimulationInputSchema
        
# Clase para validacion de datos de la solicitud de credito
class CreditRequestSchema(Schema):

    # Campos para validacion de datos de entrada en la solicitud de credito
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=100, error="El nombre supera el limite de caracteres."))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=100, error="El apellido supera el limite de caracteres."))
    email = fields.Email(required=True, error_messages={"required": "El correo electrónico es obligatorio."})
    phone = fields.Str(required=True, validate=validate.Regexp(r"^[0-9]+$", error="El número de teléfono no es válido."))
    city = fields.Str(required=True, validate=validate.Length(min=2, max=100, error="La ciudad supera el limite de caracteres."))

# Clase para validacion de datos de la solicitud de credito, hereda de CreditRequestSchema para incluir los campos de la simulacion de credito
class CreditApplicationSchema(
    SimulationInputSchema,
    CreditRequestSchema
):
    financed_amount = fields.Float(required=True, validate=validate.Range(min=0, error="El monto financiado no puede ser negativo."))
    interest_rate = fields.Float(required=True, validate=validate.Range(min=0, error="La tasa de interés no puede ser negativa."))
    monthly_payment = fields.Float(required=True, validate=validate.Range(min=0, error="El pago mensual no puede ser negativo."))
    total_interest = fields.Float(required=True, validate=validate.Range(min=0, error="El interés total no puede ser negativo."))
    total_payment = fields.Float(required=True, validate=validate.Range(min=0, error="El pago total no puede ser negativo."))