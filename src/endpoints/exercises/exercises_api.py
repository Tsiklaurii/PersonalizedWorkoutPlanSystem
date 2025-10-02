from flask_restx import abort
from flask_restx import Resource
from src.endpoints.exercises import exercises_model, exercises_ns
from src.models import Exercise
from  flask_jwt_extended import jwt_required


@exercises_ns.route("/exercises")
class ExerciseApi(Resource):

    @jwt_required()
    @exercises_ns.doc(security="JsonWebToken")
    @exercises_ns.marshal_with(exercises_model)
    def get(self):
        exercises = Exercise.query.all()
        return exercises


@exercises_ns.route('/exercise/<int:id>')
class ExercisesDetail(Resource):

    @jwt_required()
    @exercises_ns.doc(security="JsonWebToken")
    @exercises_ns.marshal_list_with(exercises_model)
    def get(self, id):
        exercise = Exercise.query.get(id)
        if not exercise:
            abort(404, message="Exercise not found")
        return exercise