from math import pow

from app.constants.vehicles import VEHICLE_RATES

# Clase para realizar el proceso de simulacion de credito
class SimulationService:
    
    # Metodo para obtener la tasa de intereses
    @staticmethod
    def get_interest_rate(vehicle_type):

        rate = VEHICLE_RATES.get(vehicle_type)

        if rate is None:
            raise ValueError("El tipo de vehículo no es válido.")

        return rate
    
    # Metodo para calcular la financiacion del vehiculo
    @staticmethod
    def calculate_financing(vehicle_value, down_payment):

        return round(vehicle_value - down_payment, 2)

    # Metodo para calcular el pago mensual utilizando la formula de amortizacion francesa
    @staticmethod
    def calculate_monthly_payment( financed_amount, interest_rate, installments):
        if interest_rate == 0:
            return round(
                financed_amount / installments,
                2
            )
        numerator = (
            interest_rate *
            pow(1 + interest_rate, installments)
        )
        denominator = (
            pow(1 + interest_rate, installments) - 1
        )
        monthly_payment = (
            financed_amount *
            (numerator / denominator)
        )

        return round(monthly_payment, 2)
    
    # Metodo para calcular el total de intereses y el total a pagar durante todo el periodo del credito
    @staticmethod
    def calculate_totals(monthly_payment, installments, financed_amount):

        total_payment = monthly_payment * installments
        total_interest = total_payment - financed_amount

        return {
            "total_interest": round(total_interest, 2),
            "total_payment": round(total_payment, 2)
        }

    # Metodo para generar el cronograma de amortizacion, mostrando el detalle de cada cuota, el pago mensual, el interes, el pago a capital y el saldo restante despues de cada pago
    @staticmethod
    def generate_amortization_schedule(financed_amount, interest_rate, installments, monthly_payment):

        balance = financed_amount
        schedule = []

        for installment in range(1, installments + 1):
            interest_payment = balance * interest_rate
            capital_payment = monthly_payment - interest_payment
            remaining_balance = balance - capital_payment

            schedule.append({
                "installment": installment,
                "monthly_payment": round(monthly_payment, 2),
                "interest": round(interest_payment, 2),
                "capital_payment": round(capital_payment, 2),
                "remaining_balance": round(max(remaining_balance, 0),2)
            })

            balance = remaining_balance

        return schedule

    # Metodo para simular el credito final
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
