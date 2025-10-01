from flask_restx import fields, reqparse
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

post_parser = reqparse.RequestParser()
post_parser.add_argument("user_id", type=int, required=True, help="User ID is required", location="json")
post_parser.add_argument("name", type=str, required=True, help="Workout plan name is required", location="json")
post_parser.add_argument("frequency", type=int, required=False, location="json")
post_parser.add_argument("goal", type=str, required=False, location="json")
post_parser.add_argument("daily_duration", type=int, required=False, location="json")

del_parser = reqparse.RequestParser()
del_parser.add_argument("id", type=int, required=True)

put_parser = post_parser.copy()
put_parser.add_argument("id", type=int, required=True)