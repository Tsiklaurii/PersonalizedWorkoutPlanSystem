from flask.cli import with_appcontext
import click

from src.ext import db
from src.models import User

def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    User(username="User1", password="password123").create()

@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("initializing database...")
    init_db()
    click.echo("Initialized database")


@click.command("populate_db")
@with_appcontext
def populate_db_command():
    populate_db()