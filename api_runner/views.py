from flask import request,render_template
from werkzeug.security import check_password_hash
from api_runner import app,lm
from .forms import LoginForm
from .models import UserInfo,CaseInfo,ProjectInfo,ModuleInfo
from flask_login import login_required,current_user,logout_user,login_user



@lm.user_loader
def load_user(id):
	return UserInfo.query.get(int(id))

@app.route('/')
@app.route('/index/')
@login_required
def index():
	return render_template('index.html')

@app.route('/api/project_list/')
@login_required
def project_list():
	return render_template('project_list.html')

@app.route('/api/add_project/')
@login_required
def add_project():
	return render_template('add_project.html')

@app.route('/api/module_list/')
@login_required
def module_list():
	return render_template('module_list.html')

@app.route('/api/add_module/')
@login_required
def add_module():
	return render_template('add_module.html')

@app.route('/api/case_list/')
@login_required
def case_list():
	return render_template('case_list.html')

@app.route('/api/add_case/')
@login_required
def add_case():
	return render_template('add_case.html')

@app.route('/api/report_list/')
@login_required
def report_list():
	return render_template('report_list.html')

@app.route('/api/settings/')
@login_required
def settings():
	return render_template('settings.html')


@app.route('/api/login/', methods=['GET','POST'])
def login():
	
	form = LoginForm()
	if form.validate_on_submit():
		username = request.form.get('username',None)
		password = request.form.get('username',None)
		remember_me = request.form.get('remember_me',None)
		user = User.query.filter_by(UserInfo.username=username).first()
		if  check_password_hash(user.password,password):
			login_user(user, remember=remember_me)
			return redirect(url_for('index'))
	return redirect(url_for('login',title='Sign In',form=form))
