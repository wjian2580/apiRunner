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
    project_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    case_id = db.relationship('case_info', backref='module_info')


class CaseInfo(db.Model):

    id = db.Column(db.String(50),primary_key=True)
    case_name = db.Column(db.String(50),unique=True)
    author = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    module_id = db.Column(db.Integer,db.ForeignKey('module_info.id'))

    






