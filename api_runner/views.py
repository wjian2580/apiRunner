from flask import render_template
from api_runner import app


@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/api/project_list/')
def project_list():
	return render_template('project_list.html')

@app.route('/api/add_project/')
def add_project():
	return render_template('add_project.html')

@app.route('/api/module_list/')
def module_list():
	return render_template('module_list.html')

@app.route('/api/add_module/')
def add_module():
	return render_template('add_module.html')

@app.route('/api/case_list/')
def case_list():
	return render_template('case_list.html')

@app.route('/api/add_case/')
def add_case():
	return render_template('add_case.html')

@app.route('/api/report_list/')
def report_list():
	return render_template('report_list.html')

@app.route('/api/settings/')
def settings():
	return render_template('settings.html')


@app.route('/api/login/')
def login():
	return render_template('login.html')