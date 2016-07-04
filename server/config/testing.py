# coding: utf-8
from .default import Config


class TestingConfig(Config):
    """Base config class."""
    TESTING = True
    SECRET_KEY = "DevelopmentConfig"

    UPLOAD_FOLDER = "/tmp/upload"
