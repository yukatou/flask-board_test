# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://yukatou:yukatou@192.168.0.12/dev_yukatou'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True



