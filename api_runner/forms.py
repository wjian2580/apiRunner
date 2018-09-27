from wtforms import StringField,BooleanField,PasswordField,SubmitField,TextAreaField,SelectField,FieldList,FormField
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo,Required,DataRequired

class LoginForm(FlaskForm):

	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
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

	module_name = StringField('模块名称',[Required()])
	belong_project = SelectField('所属项目',choices=[])
	tester = StringField('测试人员')
	desc = TextAreaField('简要描述')

class VariablesForm(FlaskForm):

	variable_type = SelectField()
	variable_key = StringField()
	variable_value = StringField()

class ParametersForm(FlaskForm):

	parameter_key = StringField()
	parameter_value = StringField()

class HooksForm(FlaskForm):

	setup_hooks = StringField()
	teardown_hooks = StringField()

class DataForm(FlaskForm):

	data_type = SelectField()
	data_key = StringField()
	data_value = StringField()

class HeadersForm(FlaskForm):

	header_key = StringField()
	header_value = StringField()

class ExtractsForm(FlaskForm):

	extract_key = StringField()
	extract_value = StringField()

class ValidatesForm(FlaskForm):

	validate_check = StringField()
	validate_comparator = SelectField()
	validate_type = SelectField()
	validate_expected = StringField()

class AddCaseForm(FlaskForm):

	case_name = StringField('用例名称')
	belong_project = SelectField('所属项目')
	belong_module = SelectField('所属模块')
	case_depend_on = SelectField('依赖用例')
	pre_condition = SelectField('前置条件')
	author = StringField('创建者')
	request_url = StringField('url')
	request_method = SelectField()
	request_type = SelectField()
	request_data = FieldList(FormField(DataForm))
	request_headers = FieldList(FormField(HeadersForm))
	extracts = FieldList(FormField(ExtractsForm))
	validates = FieldList(FormField(ValidatesForm))
	variables = FieldList(FormField(VariablesForm))
	parameters = FieldList(FormField(ParametersForm))
	hooks = FieldList(FormField(HooksForm))

		




