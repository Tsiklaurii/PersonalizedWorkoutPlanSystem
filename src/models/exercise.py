from src.ext import db
from src.models.base import BaseModel

class Exercise(BaseModel):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    instruction = db.Column(db.String)
    target_muscle = db.Column(db.String)

    workout_plan_exercises = db.relationship("WorkoutPlanExercise", back_populates="exercise")