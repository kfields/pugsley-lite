from flask import Blueprint

bp = Blueprint('schedule', __name__, template_folder='templates')

from pugsley.schedule import routes
