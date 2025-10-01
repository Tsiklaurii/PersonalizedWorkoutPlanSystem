from src.ext import db
from src.models.base import BaseModel

class WorkoutPlanExercise(BaseModel):
    __tablename__ = "workout_plan_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey("workout_plans.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)
    sets = db.Column(db.Integer)
    repetitions = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    distance = db.Column(db.Float)

    exercise = db.relationship("Exercise", back_populates="workout_plan_exercises")
    workout_plan = db.relationship("WorkoutPlan", back_populates="workout_plan_exercises")