import os


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DEBUG = True
    APPINSIGHTS_INSTRUMENTATIONKEY = None
    SECRET_KEY = 'somekey'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', TestingConfig.SQLALCHEMY_DATABASE_URI)
    APPINSIGHTS_INSTRUMENTATIONKEY = os.environ.get('APPINSIGHTS_INSTRUMENTATIONKEY', TestingConfig.APPINSIGHTS_INSTRUMENTATIONKEY)
    SECRET_KEY = os.environ.get('SECRET_KEY', TestingConfig.SECRET_KEY)
    