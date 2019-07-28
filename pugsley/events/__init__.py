from flask import Blueprint

bp = Blueprint('events', __name__, template_folder='templates')

from pugsley.events import routes
