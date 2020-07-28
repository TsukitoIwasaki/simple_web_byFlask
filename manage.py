from __future__ import print_function

from flask_script import Manager
from flask_script import Server

from flaskr import app
from flaskr import db


manager = Manager(app)

manager.add_command(
    "runserver", 
    Server(
    use_debugger = True,
    use_reloader = True,
    ) 
)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()