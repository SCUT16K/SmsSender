# coding: utf-8
from .default import Config


class DevelopmentConfig(Config):
    """Base config class."""
    TESTING = False
    SECRET_KEY = "DevelopmentConfig"

    # Site domain
    SITE_TITLE = "flask-usage"

    # SQL CONFIG
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:Password@localhost/sms"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOAD_FOLDER = "/tmp/upload"
