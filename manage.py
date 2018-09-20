from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from api_runner import app,db
from api_runner.models import User,ProjectInfo,ModuleInfo,CaseInfo

migrate = Migrate(app,db)

manager = Manager(app)

manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
	return dict(app=app,db=db,User=User,ProjectInfo=ProjectInfo,ModuleInfo=ModuleInfo,CaseInfo=CaseInfo)


if __name__ == '__main__':
	manager.run()