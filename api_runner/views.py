from flask import request,render_template,redirect,url_for,flash,jsonify,session,abort
from werkzeug.security import check_password_hash,generate_password_hash
from api_runner import app,lm,db
from datetime import datetime
from .forms import LoginForm,ChangePasswordForm,AddProjectForm,AddModuleForm,AddCaseForm,EditProjectForm,EditModuleForm
from .models import User,CaseInfo,ProjectInfo,ModuleInfo
from flask_login import login_required,current_user,logout_user,login_user



@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')


@app.context_processor
def test_context():
	temp = '''
	<ul>
		<li>heheheh</li>
		<li>heiehi</li>
		<li>haha</li>
	</ul>
		
		'''
	return dict(temp=temp)


@app.route('/api/project_list/')
@login_required
def project_list():
	app.logger.info('project_list viewing')
	projects = ProjectInfo.query.all()
	if request.is_xhr:
		return jsonify([(project.id,project.project_name) for project in projects])
	return render_template('project_list.html', projects=projects)

@app.route('/api/add_project/',methods=['POST','GET'])
@login_required
def add_project():
	form = AddProjectForm()
	if form.validate_on_submit():
		project = ProjectInfo(
			project_name=form.project_name.data,
			manager=form.manager.data,
			desc=form.desc.data,
			create_time=datetime.now(),
			update_time=datetime.now()
			)
		db.session.add(project)
		db.session.commit()
		return redirect(url_for('project_list'))
	return render_template('add_project.html',form=form)

@app.route('/api/edit_project/<int:project_id>', methods=['POST', 'GET'])
@login_required
def edit_project(project_id):
	form = EditProjectForm()
	project = ProjectInfo.query.get(project_id)
	if form.validate_on_submit():
		project.project_name = form.project_name.data
		project.manager = form.manager.data
		project.desc = form.desc.data
		project.update_time = datetime.now()
		db.session.commit()
		return redirect(url_for('project_list'))
	form.project_name.data = project.project_name
	form.manager.data = project.manager
	form.desc.data = project.desc
	return render_template('edit_project.html', form=form)

@app.route('/api/delete_project/<int:project_id>', methods = ['POST'])
@login_required
def delete_project(project_id):
	project = ProjectInfo.query.get(project_id)
	if project:
		db.session.delete(project)
		db.session.commit()
		return jsonify({'success':'true'}),200
	else:
		abort(400)

@app.route('/api/add_module/',methods=['POST','GET'])
@login_required
def add_module():
	form = AddModuleForm()
	if form.validate_on_submit():
		module = ModuleInfo(
			module_name=form.module_name.data,
			project_id=form.belong_project.data,
			tester=form.tester.data,
			desc=form.desc.data,
			create_time=datetime.now(),
			update_time=datetime.now()
			)
		db.session.add(module)
		db.session.commit()
		return redirect(url_for('module_list'))
	return render_template('add_module.html',form=form)

@app.route('/api/edit_module/<int:module_id>',methods=['POST','GET'])
@login_required
def edit_module(module_id):
	form = EditModuleForm()
	module = ModuleInfo.query.get(module_id)
	if form.validate_on_submit():
		module.module_name=form.module_name.data
		module.tester=form.tester.data
		module.desc=form.desc.data
		module.update_time=datetime.now()
		db.session.commit()
		return redirect(url_for('module_list'))
	form.module_name.data = module.module_name
	form.tester.data = module.tester
	form.desc.data = module.desc
	return render_template('edit_module.html',form=form)

@app.route('/api/delete_module/<int:module_id>',methods=['POST'])
@login_required
def delete_module(module_id):
	module = ModuleInfo.query.get(module_id)
	if module:
		db.session.delete(module)
		db.session.commit()
		return jsonify({'success':'true'}),200
	else:
		abort(400)

@app.route('/api/module_list/')
@login_required
def module_list():
	modules = ModuleInfo.query.all()
	return render_template('module_list.html',modules=modules)

@app.route('/api/modules/<int:project_id>')
@login_required
def modules(project_id):
	modules = ProjectInfo.query.get(project_id).modules
	return jsonify([(module.id,module.module_name) for module in modules])

@app.route('/api/cases/<int:module_id>')
@login_required
def cases(module_id):
	cases = ModuleInfo.query.get(module_id).cases
	return jsonify([(case.id,case.case_name) for case in cases])

@app.route('/api/case_list/')
@login_required
def case_list():
	return render_template('case_list.html')

@app.route('/api/add_case/',methods=['POST','GET'])
@login_required
def add_case():
	form = AddCaseForm()
	if form.validate_on_submit():
		pass
	projects = ProjectInfo.query.all()
	project_choices = [(project.id,project.project_name) for project in projects]
	form.belong_project.choices = project_choices
	form.request_method.choices = [('GET','GET'),('POST','POST'),('PUT','PUT'),('DELETE','DELETE')]
	form.request_type.choices = [('data','data'),('json','json'),('params','params')]
	form.belong_module.choices = []
	form.case_depend_on.choices = [('0','无依赖')]
	form.pre_condition.choices = [('0','无前置条件')]
	if projects:
		modules = projects[0].modules
		module_choices = [(module.id,module.module_name) for module in modules]
		form.belong_module.choices = module_choices
		if modules:
			cases = modules[0].cases
			case_choices = [(case.id,case.case_name) for case in cases]
			form.case_depend_on.choices += case_choices
	return render_template('add_case.html',form=form)

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
	form = LoginForm(request.form)
	if form.validate_on_submit():
		username = request.form.get('username',None)
		password = request.form.get('password',None)
		remember_me = request.form.get('remember_me',None)
		user = User.query.filter(User.username==username).first()
		if user:
			if check_password_hash(user.password,password):
				login_user(user, remember=remember_me)
				session['logged_in'] = True
				return redirect(url_for('index'))
		flash('用户名或密码错误')
	return render_template('login.html',title='Sign In',form=form)

@app.route('/api/logout/')
@login_required
def logout():
	session.pop('logged_in')
	logout_user()
	return redirect(url_for('login'))

@app.route('/api/change_password/',methods=['GET','POST'])
@login_required
def change_password():
	form = ChangePasswordForm() 
	if form.validate_on_submit():
		old_password = request.form.get('old_password',None)
		new_password = request.form.get('new_password',None)
		if check_password_hash(current_user.password, old_password):
			new_password = generate_password_hash(new_password)
			current_user.password = new_password
			current_user.update_time = datetime.now()
			db.session.add(current_user)
			db.session.commit()
			flash('密码修改成功')
			return redirect(url_for('index'))
		else:
			flash('当前密码输入错误')
	return render_template('change_password.html',title='ApiRunner-Change-Password',form=form)



@app.errorhandler(404)
def page_not_found(e):
	return render_template('errors/404.html'),404


def get_next_url(default='index', **kwargs):
	for url in request.args.get('next'),request.referrer:
		if url:
			return redirect(url)
	return redirect(url_for(default, **kwargs))




