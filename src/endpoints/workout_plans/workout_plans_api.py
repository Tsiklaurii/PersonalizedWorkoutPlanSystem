from flask_restx import abort
from flask_restx import Resource
from src.endpoints.workout_plans import workout_plans_ns, workout_plans_model, post_parser, del_parser, put_parser
from src.models import WorkoutPlan


@workout_plans_ns.route("/workout_plans")
class WorkoutPlansApi(Resource):
    @workout_plans_ns.marshal_with(workout_plans_model)
    def get(self):
        workout_plans = WorkoutPlan.query.all()
        return workout_plans

    @workout_plans_ns.doc(parser=post_parser)
    @workout_plans_ns.marshal_with(workout_plans_model)
    def post(self):
        args = post_parser.parse_args()

        workout_plan = WorkoutPlan(
            user_id=args["user_id"],
            name=args["name"],
            frequency=args.get("frequency"),
            goal=args.get("goal"),
            daily_duration=args.get("daily_duration")
        )
        workout_plan.create()
        return workout_plan, 201

    @workout_plans_ns.doc(parser=put_parser)
    @workout_plans_ns.marshal_with(workout_plans_model)
    def put(self):
        args = put_parser.parse_args()

        workout_plan = WorkoutPlan.query.get(args.get("id"))
        if not workout_plan:
            return {"message": "Workout plan not found"}, 404

        workout_plan.user_id = args.get("user_id", workout_plan.user_id)
        workout_plan.name = args.get("name", workout_plan.name)
        workout_plan.frequency = args.get("frequency", workout_plan.frequency)
        workout_plan.goal = args.get("goal", workout_plan.goal)
        workout_plan.daily_duration = args.get("daily_duration", workout_plan.daily_duration)

        workout_plan.save()
        return workout_plan, 200

    @workout_plans_ns.doc(parser=del_parser)
    def delete(self):
        args = del_parser.parse_args()
        workout_plan = WorkoutPlan.query.get(args["id"])
        if not workout_plan:
            return {"message": "Workout plan not found"}, 404

        workout_plan.delete()
        workout_plan.save()
        return {"message": "Success"}, 200


@workout_plans_ns.route('/workout_plan/<int:id>')
class WorkoutPlanDetail(Resource):
    @workout_plans_ns.marshal_with(workout_plans_model)
    def get(self, id):
        workout_plan = WorkoutPlan.query.get(id)
        if not workout_plan:
            abort(404, message="Workout plan not found")
        return workout_plan