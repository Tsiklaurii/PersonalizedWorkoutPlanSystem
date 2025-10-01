# from flask_restx import abort
from flask_restx import Resource
from src.endpoints.workout_plans import workout_plans_ns, workout_plans_model
from src.models import WorkoutPlan


@workout_plans_ns.route("/workout_plans")
class WorkoutPlansApi(Resource):
    @workout_plans_ns.marshal_with(workout_plans_model)
    def get(self):
        workout_plans = WorkoutPlan.query.all()
        return workout_plans


# @workout_plans_ns.route('/exercise/<int:id>')
# class ExercisesDetail(Resource):
#     @workout_plans_ns.marshal_list_with(exercises_model)
#     def get(self, id):
#         exercise = Exercise.query.get(id)
#         if not exercise:
#             abort(message="Exercise not found")
#         return exercise