from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLAlchemy'] = 'mysql://root:1234@47.94.23.2/HttpRunner'
db = SQLAlchemy(app)

from api_runner import views