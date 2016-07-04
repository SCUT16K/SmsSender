# coding: utf-8
from .default import Config


class DockerConfig(Config):
    """Base config class."""
    TESTING = False
    SECRET_KEY = "DockerConfig"

    # Site domain
    SITE_TITLE = "flask-usages"

    UPLOAD_FOLDER = "/tmp/upload"
