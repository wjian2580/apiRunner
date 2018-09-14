from api_runner import db, app
from datetime import datetime


class UserInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)


class ProjectInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), unique=True)
    manager = db.Column(db.String(50))
    tester = db.Column(db.String(50))
    dev = db.Column(db.String(50))
    desc = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    module_id = db.relationship('module_info', backref='project_info')


class ModuleInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(50), unique=True)
    tester = db.Column(db.String(50))
    dev = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    project_id = db.Column(db.String(50), db.ForeignKey('user_info.id')
    test = db.Column()





