from app.config.db import db
from app.models.credit_request import CreditRequest

class CreditRequestService:

    @staticmethod
    def create_credit_request(personal_data, simulation_data):

        credit_request = CreditRequest(
            **personal_data,
            **simulation_data
        )

        db.session.add(credit_request)
        db.session.commit()

        return credit_request

    @staticmethod
    def get_all_requests():

        return CreditRequest.query.order_by(CreditRequest.created_at.desc()).all()

    @staticmethod
    def get_request_by_id(request_id):

        return CreditRequest.query.get(request_id)