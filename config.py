import os

class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY = os.urandom(32)
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    


class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
   if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
 #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)   
       

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:moringa@localhost/blog_test'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:moringa@localhost/blog'

    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
