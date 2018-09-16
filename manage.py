from flask_script import Manager,Server
from api_runner import app,db
from api_runner.models import UserInfo,ProjectInfo,ModuleInfo,CaseInfo

manager = Manager(app)

manager.add_command('server', Server())

@manager.shell
def make_shell_context():
	return dict(app=app,db=db,UserInfo=UserInfo,ProjectInfo=ProjectInfo,ModuleInfo=ModuleInfo,CaseInfo=CaseInfo)


if __name__ == '__main__':
	manager.run()