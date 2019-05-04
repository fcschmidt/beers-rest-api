import os

project_name = 'beers'


class Config:
    DEBUG = os.getenv('DEBUG') or False
    DEFAULT_DATABASE = f'sqlite:////var/tmp/{project_name}_dev.sqlite'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or DEFAULT_DATABASE
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG


class Development(Config):
    """Development environment configuration"""
    DEBUG = True


class Production(Config):
    """Production environment configurations"""
    DEBUG = False
    TESTING = False


class Testing(Config):
    """Testing environment configurations"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:////tmp/{project_name}_test.sqlite'


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
