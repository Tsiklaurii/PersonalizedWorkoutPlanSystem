from flask_restx import Resource
from src.models import User
from src.endpoints.auth import auth_ns, register_parser

@auth_ns.route("/register")
class RegisterApi(Resource):

    @auth_ns.doc(parser=register_parser)
    def post(self):
        args = register_parser.parse_args()
        username = args["username"]
        password = args["password"]

        if User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 400

        new_user = User(username=username, password=password)
        new_user.create()

        return {"message": "User created successfully"}, 201