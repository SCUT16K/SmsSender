# coding: utf-8
from .default import Config


class ProductionConfig(Config):
    # Site domain
    SITE_DOMAIN = "http://www.twtf.com"

    # Db config
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dbuser:dbpass@localhost/databasename"

    # Sentry
    SENTRY_DSN = ''
