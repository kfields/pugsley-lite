from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('auth', __name__)
CORS(bp)
from pugsley.auth import routes
