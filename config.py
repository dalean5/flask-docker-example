import os
basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_variable(var_name, type='str'):
    """Get the environment variable or return an exception"""
    try:
        value = os.environ[var_name]
        if type == 'str':
            return str(value)
        if type == 'int':
            return int(value)
        if type ==' bool':
            return bool(value)

        raise ValueError('Type of "{}" is invalid'.format(type))
            
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ValueError(error_msg)


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = get_env_variable('SECRET_KEY')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True