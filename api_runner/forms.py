from wtforms import StringField,BooleanField,PasswordField,SubmitField,TextAreaField,SelectField
from flask_wtf import FlaskForm,Form
from wtforms.validators import EqualTo,Required

class LoginForm(FlaskForm):

	username = StringField(validators=[Required()])
	password = PasswordField(validators=[Required()])
	remember_me = BooleanField('记住登录信息', default=False)


class ChangePasswordForm(FlaskForm):

	old_password = PasswordField('当前密码',validators=[Required()])
	new_password = PasswordField('新密码',validators=[Required(),EqualTo('confirm_password',message='两次密码不一致')])
	confirm_password = PasswordField('确认密码',validators=[Required()])
	submit = SubmitField('提交')

class AddProjectForm(FlaskForm):

	project_name = StringField('项目名称',validators=[Required()])
	manager = StringField('负责人',validators=[Required()])
	desc = TextAreaField('简要描述')
	submit = SubmitField('提交')

class AddModuleForm(FlaskForm):

	module_name = StringField('模块名称')
	belong_project = SelectField('所属项目',choices=[])
	tester = StringField('测试人员')
	desc = TextAreaField('简要描述')

class AddCaseForm(FlaskForm):

	case_name = StringField('用例名称')
	belong_project = SelectField('所属项目')
	belong_module = SelectField('所属项目')
	case_depend_on = SelectField('所属项目')
	author = StringField('所属项目')
		

