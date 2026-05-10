from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import JSONB
from app.config.db import db

class CreditRequest(db.Model):
    __tablename__ = 'credit_requests'

    # LLave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Informacion personal
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    # Informacion del credito
    vehicle_type = db.Column(db.String(50), nullable=False)
    vehicle_value = db.Column(db.Float, nullable=False)
    down_payment = db.Column(db.Float, nullable=False)
    financed_amount = db.Column(db.Float, nullable=False)
    installments = db.Column(db.Integer, nullable=False)
    amortization_schedule = db.Column(JSONB, nullable=True)
    interest_rate = db.Column(db.Float, nullable=False)
    monthly_payment = db.Column(db.Float, nullable=False)
    total_interest = db.Column(db.Float, nullable=False)
    total_payment = db.Column(db.Float, nullable=False)

    # Timestamps
    updated_at = db.Column(db.DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc),nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,

            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "city": self.city,

            "vehicle_type": self.vehicle_type,
            "vehicle_value": round(self.vehicle_value, 2),
            "down_payment": round(self.down_payment, 2),
            "financed_amount": round(self.financed_amount, 2),
            "installments": self.installments,
            "amortization_schedule": self.amortization_schedule,
            "interest_rate": round(self.interest_rate, 4),
            "monthly_payment": round(self.monthly_payment, 2),
            "total_interest": round(self.total_interest, 2),
            "total_payment": round(self.total_payment, 2),

            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    def __repr__(self):
        return (
            f"<CreditRequest "
            f"id={self.id} "
            f"email={self.email} "
            f"vehicle={self.vehicle_type}>"
        )