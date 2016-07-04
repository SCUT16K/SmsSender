#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import logging
import logging.handlers

from flask import Flask

from config import load_config
from application.extentions import db, migrate
from application.controllers.sms import SmsView


# convert python's encoding to utf8
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass


def create_app(mode):
    """Create Flask app."""
    print "mode: {}".format(mode)
    config = load_config(mode)

    app = Flask(__name__)
    app.config.from_object(config)

    if not hasattr(app, 'production'):
        app.production = not app.debug and not app.testing

    # Register components
    configure_logging(app)
    register_view(app)
    register_extensions(app)

    return app


def register_view(app):
    app.add_url_rule('/sms', view_func=SmsView.as_view('sms'))


def register_extensions(app):
    """config extensions"""
    db.init_app(app)
    migrate.init_app(app, db)


def configure_logging(app):
    """config logging"""
    logging.basicConfig()
    if app.config.get('TESTING'):
        app.logger.setLevel(logging.INFO)
        return
    elif app.config.get('DEBUG'):
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)

    # make dir if /tmp/logs not exists
    if not os.path.isdir(app.config["LOG_DIR"]):
        os.makedirs(app.config["LOG_DIR"])
    info_log = os.path.join(app.config["LOG_DIR"], "running.info")
    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log, maxBytes=104857600, backupCount=2)
    info_file_handler.setLevel(logging.DEBUG)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)
