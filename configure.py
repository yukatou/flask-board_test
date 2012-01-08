# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    SECRET_KEY = 'development key'
    SQLALCHEMY_DATABASE_URI = 'mysql://yukatou:yukatou@192.168.0.12/dev_yukatou'

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://yukatou:yukatou@192.168.0.12/dev_yukatou'

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://yukatou:yukatou@192.168.0.12/dev_yukatou'

class Test(Config):
    TESTING = True



