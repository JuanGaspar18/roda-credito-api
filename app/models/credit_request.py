from datetime import datetime, timezone
from app.config.db import db

class CreditRequest(db.Model):
    __tablename__ = 'credit_requests'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    vehicle_value = db.Column(db.Float, nullable=False)
    down_payment = db.Column(db.Float, nullable=False)
    financed_amount = db.Column(db.Float, nullable=False)
    installments = db.Column(db.Integer, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    monthly_payment = db.Column(db.Float, nullable=False)
    total_interest = db.Column(db.Float, nullable=False)
    total_payment = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc),nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
