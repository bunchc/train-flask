import click
from flask.cli import FlaskGroup
from flask_migrate import MigrateCommand

from trainapi.app import create_app


def create_trainapi(info):
    return create_app()


@click.group(cls=FlaskGroup, create_app=create_trainapi)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from trainapi.extensions import db
    from trainapi.models import User
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


@cli.command()
def db():
    """Flask-migrate integration"""
    MigrateCommand()


if __name__ == "__main__":
    cli()
