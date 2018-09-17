from wtforms import StringField,BooleanField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	remember_me = BooleanField('记住登录信息', default=False)

