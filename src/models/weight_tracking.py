from datetime import datetime
from src.ext import db
from src.models.base import BaseModel

class WeightTrack (BaseModel):
    __tablename__ = 'weight_tracking'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    weight = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="weight_tracking")