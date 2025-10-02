from flask_restx import fields, reqparse
from src.ext import api

weight_tracking_ns = api.namespace("WeightTrack", path='/api')

weight_tracking_model = weight_tracking_ns.model("WeightTrack", {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "weight": fields.Integer,
    "date": fields.DateTime
})

post_parser = reqparse.RequestParser()
post_parser.add_argument("weight", type=int, required=True, location="json")