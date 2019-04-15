from flask import Blueprint

bp = Blueprint('graphql', __name__, template_folder='templates')

from pugsley.graphql import routes
