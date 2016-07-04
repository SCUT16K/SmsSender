# coding: utf-8
from .default import Config


class ProductionConfig(Config):
    # Site domain
    SITE_DOMAIN = "http://www.liuliqiang.info"

    # Db config
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost/flask-usages"

    # Sentry
    SENTRY_DSN = ''
