#!/usr/bin/env python
# encoding: utf-8
import sys
import subprocess

from flask_script import Manager
from flask_script.commands import ShowUrls
from flask.ext.migrate import MigrateCommand

from application import create_app
from application.extentions import db
from utils.commands import GEventServer, ProfileServer


manager = Manager(create_app)
manager.add_option('-c', '--config', dest='mode', required=False)

manager.add_command("showurls", ShowUrls())
manager.add_command("gevent", GEventServer())
manager.add_command("profile", ProfileServer())
manager.add_command('db', MigrateCommand)


@manager.option('-c', '--config', help='enviroment config')
def simple_run(config):
    app = create_app(config)
    app.run(host="0.0.0.0", port=9192, debug=True)


@manager.command
def lint():
    """Runs code linter."""
    lint = subprocess.call(['flake8', '--ignore=E402,F403,E501', 'application/',
                            'manage.py', 'tests/']) == 0
    if lint:
        print('OK')
    sys.exit(lint)


@manager.command
def test():
    """Runs unit tests."""
    tests = subprocess.call(['python', '-c', 'import tests; tests.run()'])
    sys.exit(tests)


@manager.command
def create_db():
    """create tables"""
    db.create_all()


if __name__ == "__main__":
    manager.run()
