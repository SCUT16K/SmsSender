# coding: utf-8
import os


class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "sample_key"

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Site domain
    SITE_DOMAIN = "http://localhost:8080"

    # log dir
    LOG_DIR = "/tmp/logs"
