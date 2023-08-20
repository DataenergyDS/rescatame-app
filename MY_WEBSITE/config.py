import os 
basedir = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Bak1ro_del_m0Nt5'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLAlCHEMY_TRACK_MODIFICATIONS = False
