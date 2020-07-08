from app import create_app
from flask_script import Manager,Shell,Server
from app import create_app,db
from app.models import User,Role

# Creating app instance
app = create_app('development')
manager = Manager(app)

manager.add_command('server',Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role )

if __name__ == '__main__':
    manager.run()
