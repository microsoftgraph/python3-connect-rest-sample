#!/usr/bin/env python
from flask_script import Manager, Shell, Server
from connect import app

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())
manager.run()
