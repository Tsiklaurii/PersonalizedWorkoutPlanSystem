from src.ext import db
from src.models.base import BaseModel

class WorkoutPlan(BaseModel):
    __tablename__ = "workout_plans"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.Integer)
    goal = db.Column(db.String(255))
    daily_duration = db.Column(db.Integer)

    user = db.relationship("User", back_populates="workout_plans")
    workout_plan_exercises = db.relationship(
        "WorkoutPlanExercise",
        back_populates="workout_plan",
        cascade="all, delete-orphan"
    )