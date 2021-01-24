import os

basedir = os.path.abspath(os.path.dirname(__file__))

class LocalConfig():
    ENV = "development"
    TESTING = True
    DEBUG = True