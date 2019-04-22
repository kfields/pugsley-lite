from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('mc', __name__)
CORS(bp)

from pugsley.mc import routes
