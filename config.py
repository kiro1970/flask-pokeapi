import os

basedir = os.path.abspath(os.path.dirname(__name__))
print('BASEDIR==' + basedir)

class Config:
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRECT_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True