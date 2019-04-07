from flask import Blueprint

bp = Blueprint('main', __name__)

from pugsley.main import routes
