from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Post,Comments

app=create_app('dev')
run = Manager(app)
migrate = Migrate(app,db)
run.add_command('server',Server)
run.add_command('db',MigrateCommand)

@run.shell
def make_shell_context():
  return dict(app=app,db=db, User=User,Comments=Comments,Post=Post)

@run.command
def test():
  '''
  Unittests
  '''
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
  run.run()


  