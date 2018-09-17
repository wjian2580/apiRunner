from wtforms import StringField,BooleanField,PasswordField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo

class LoginForm(FlaskForm):

	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	remember_me = BooleanField('记住登录信息', default=False)


class ChangePasswordForm(FlaskForm):

	old_password = PasswordField('当前密码',validators=[DataRequired()])
	new_password = PasswordField('新密码',validators=[DataRequired(),EqualTo('confirm_password',message='两次密码不一致')])
	confirm_password = PasswordField('确认密码',validators=[DataRequired()])
	submit = SubmitField('提交')

