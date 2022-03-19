"""
Add a management command here
"""

import click
from flask.cli import AppGroup

from app.models.auth import User

from werkzeug.security import generate_password_hash, check_password_hash


# flask manage <command>
management_command = AppGroup('manage')

@management_command.command('create_user')
@click.argument('name')
@click.argument('password')
def create_user(name, password):
    """
    Create auth user and password
    usage: flask manage create_user <username> <password>
    """
    u = User(username=name, password=generate_password_hash(password))
    u.save()
