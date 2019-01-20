import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.jinja_env.trim_blocks=True
app.jinja_env.lstrip_blocks=True
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
db = SQLAlchemy(app)
lm = LoginManager()
lm.session_protection='strong'
lm.login_view='login'
lm.init_app(app)

from api_runner import views


def register_log():
	app.logger.setLevel(logging.INFO)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	file_handler = RotatingFileHandler('logs/api_runner.log', maxBytes=10*1024*1024, backupCount=10)
	file_handler.setFormatter(formatter)
	file_handler.setLevel(Logging.INFO)

	if not app.debug:
		app.logger.addHandler(file_handler)
