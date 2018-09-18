from wtforms import StringField,BooleanField,PasswordField,SubmitField,TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo,Required

class LoginForm(FlaskForm):

	username = StringField(validators=[Required()])
	password = PasswordField(validators=[Required()])
	remember_me = BooleanField('记住登录信息', default=False)


class ChangePasswordForm(FlaskForm):

	old_password = PasswordField('当前密码',[Required()])
	new_password = PasswordField('新密码',[Required(),EqualTo('confirm_password',message='两次密码不一致')])
	confirm_password = PasswordField('确认密码',[Required()])
	submit = SubmitField('提交')

class AddProjectForm(FlaskForm):

	project_name = StringField('项目名称',[Required()])
	manager = StringField('负责人',[Required()])
	tester = StringField('测试人员',[Required()])
	dev = StringField('开发人员',[Required()])
	desc = TextAreaField('简要描述')
	submit = SubmitField('提交')
		

