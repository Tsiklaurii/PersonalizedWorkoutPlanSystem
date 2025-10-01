from flask import Flask
from src.commands import init_db_command, populate_db_command
from src.config import Config
from src.ext import db, migrate, api
from src.endpoints import ExerciseApi, WorkoutPlansApi, WeightTrackingApi

COMMANDS = [init_db_command, populate_db_command]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    #Flask-RestX
    api.init_app(app)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)