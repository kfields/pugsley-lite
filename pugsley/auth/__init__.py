from flask import Blueprint

bp = Blueprint('auth', __name__)

from pugsley.auth import routes
