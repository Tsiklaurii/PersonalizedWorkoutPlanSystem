from flask_restx import Resource
from src.endpoints.weight_tracking import weight_tracking_ns, weight_tracking_model, post_parser
from src.models import WeightTrack


@weight_tracking_ns.route("/weight_tracking")
class WeightTrackingApi(Resource):

    @weight_tracking_ns.marshal_with(weight_tracking_model)
    def get(self):
        weight_track = WeightTrack.query.all()
        return weight_track

    @weight_tracking_ns.doc(parser=post_parser)
    @weight_tracking_ns.marshal_with(weight_tracking_model)
    def post(self):
        args = post_parser.parse_args()

        weight_tracking = WeightTrack(
            user_id=args["user_id"],
            weight=args["weight"],
            date=args.get("date")
        )
        weight_tracking.create()
        return weight_tracking, 201