from flask import Blueprint

bp = Blueprint('auth', __name__)

from lib.auth import routes
