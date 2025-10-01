from werkzeug.security import generate_password_hash, check_password_hash
from src.ext import db
from src.models.base import BaseModel

class User (BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password = db.Column(db.String)

    workout_plans = db.relationship("WorkoutPlan", back_populates="user")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)