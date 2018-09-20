from api_runner import db, app
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)


class ProjectInfo(db.Model):

    __tablename__ = 'project_info'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), unique=True)
    manager = db.Column(db.String(50))
    tester = db.Column(db.String(50))
    dev = db.Column(db.String(50))
    desc = db.Column(db.String(200))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    cases = db.relationship('CaseInfo', backref='project_info')
    modules = db.relationship('ModuleInfo', backref='project_info')


class ModuleInfo(db.Model):

    __tablename__ = 'module_info'

    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(50), unique=True)
    tester = db.Column(db.String(50))
    dev = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey('project_info.id'))
    cases = db.relationship('CaseInfo', backref='module_info')


class CaseInfo(db.Model):

    __tablename__ = 'case_info'

    id = db.Column(db.Integer,primary_key=True)
    case_name = db.Column(db.String(50),unique=True)
    author = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    module_id = db.Column(db.Integer,db.ForeignKey('module_info.id'))
    project_id = db.Column(db.Integer,db.ForeignKey('project_info.id'))


class ConfigInfo(db.Model):

    __tablename__ = 'config_info'

    id = db.Column(db.Integer,primary_key=True)
    config_name = db.Column(db.String(50),unique=True)


    






