from flask import render_template
from api_runner import app


@app.route('/')
@app.route('/index/')
def index():

	return render_template('index.html')

@app.route('/api/project_list/')
def project_list():

	return render_template('project_list.html')

