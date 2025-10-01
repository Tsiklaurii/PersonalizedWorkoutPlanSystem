from flask_restx import fields

from src.ext import api

workout_plans_ns = api.namespace("WorkoutPlans", path='/api')

workout_plans_model = workout_plans_ns.model("WorkoutPlan", {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "name": fields.String,
    "frequency": fields.Integer,
    "goal": fields.String,
    "daily_duration":fields.Integer
})