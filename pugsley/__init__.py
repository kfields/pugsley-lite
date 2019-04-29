from flask import Flask, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

mail = Mail(app)
babel = Babel(app)
bootstrap = Bootstrap(app)

from pugsley.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from pugsley.main import bp as main_bp
app.register_blueprint(main_bp)

from pugsley.schedule import bp as schedule_bp
app.register_blueprint(schedule_bp)

from pugsley.graphql import bp as graphql_bp
app.register_blueprint(graphql_bp)

from pugsley import models