from flask import Blueprint

bp = Blueprint('main', __name__)

from lib.main import routes
