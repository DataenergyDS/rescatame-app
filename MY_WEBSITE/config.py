import os 


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Bak1ro_del_m0Nt5'