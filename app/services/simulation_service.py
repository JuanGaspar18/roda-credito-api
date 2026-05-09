from math import pow

# Clase para realizar el proceso de simulacion de credito
class SimulationService:

    VEHICLE_RATES = {
            "Bicicleta electrica": 0.05,
            "Moto electrica": 0.013
        }
    
    # Metodo para obtener la tasa de intereses
    @staticmethod
    def get_interest_rate(cls, vehicle_type):

        if vehicle_type not in cls.VEHICLE_RATES:
            raise ValueError("El tipo de vehículo no es válido.")

        return cls.VEHICLE_RATES.get(vehicle_type)  # Tasa de interés para el tipo de vehículo especificado
    
    # Metodo para calcular la financiacion del vehiculo
    @staticmethod
    def calculate_financing(vehicle_value, down_payment):

        financed_amount = vehicle_value - down_payment

        return round(financed_amount, 2)

    @staticmethod
    def calculate_monthly_payment(financed_amount, interest_rate, installments):

        monthly_payment = financed_amount * (interest_rate * pow(1 + interest_rate, installments)) / (pow(1 + interest_rate, installments) - 1)

        return round(monthly_payment, 2)
    
    @staticmethod
    def calculate_totals(monthly_payment, installments, financed_amount):

        total_payment = monthly_payment * installments
        total_interest = total_payment - financed_amount

        return round(total_payment, 2), round(total_interest, 2)

    @staticmethod
    def generate_amortization_schedule(
        financed_amount,
        interest_rate,
        installments,
        monthly_payment
    ):

        balance = financed_amount
        schedule = []

        for installment_number in range(1, installments + 1):
            interest = balance * interest_rate
            capital_payment = monthly_payment - interest
            remaining_balance = balance - capital_payment

            schedule.append({
                "installment": installment_number,
                "monthly_payment": round(monthly_payment, 2),
                "interest": round(interest, 2),
                "capital_payment": round(capital_payment, 2),
                "remaining_balance": round(max(remaining_balance, 0),2)
            })

            balance = remaining_balance

        return schedule

    @classmethod
    def simulate_credit(cls, vehicle_type, vehicle_value, down_payment, installments):
        
        interest_rate = cls.get_interest_rate(vehicle_type)
        financed_amount = cls.calculate_financing(vehicle_value, down_payment)
        monthly_payment = cls.calculate_monthly_payment(financed_amount, interest_rate, installments)
        totals = cls.calculate_totals(monthly_payment, installments, financed_amount)
        amortization_schedule = cls.generate_amortization_schedule(financed_amount, interest_rate, installments, monthly_payment)

        return {
            "vehicle_type": vehicle_type,
            "vehicle_value": round(vehicle_value, 2),
            "down_payment": round(down_payment, 2),
            "financed_amount": financed_amount,
            "interest_rate": interest_rate,
            "installments": installments,
            "monthly_payment": monthly_payment,
            "total_interest": totals["total_interest"],
            "total_payment": totals["total_payment"],
            "amortization_schedule": amortization_schedule
        }
