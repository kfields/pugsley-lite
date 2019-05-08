from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('filepond', __name__)
CORS(bp)
from pugsley.filepond import routes
