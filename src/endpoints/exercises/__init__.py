from flask_restx import fields

from src.ext import api

exercises_ns = api.namespace("Exercises", path='/api')

exercises_model = exercises_ns.model("Exercise", {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "instruction": fields.String,
    "target_muscle": fields.String,
})