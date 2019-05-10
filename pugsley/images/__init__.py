from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('images', __name__)
CORS(bp)
from pugsley.images import routes
