import os

WTF_CSRF_ENABLED = True
# You should change this
SECRET_KEY = 'a-very-secret-secret'


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

