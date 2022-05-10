import os


class Config():
    
    
    SECRET_KEY = os.environ['SECRET_KEY']
    HOSTNAME = os.environ['HOSTNAME']
    DBUSERNAME = os.environ['DBUSERNAME']
    DBPASSWORD = os.environ['DBPASSWORD']
    DBNAME = os.environ['DBNAME']
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@localhost/{}'.format(DBUSERNAME,DBPASSWORD,DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    EMAIL_SERVER = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TSL = True
    USER_NAME = os.environ['USER_NAME']
    USER_PASS = os.environ['USER_PASS']







class DevConfig(Config):

  DEBUG = True


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

  

config_options = {
  'dev': DevConfig,
  'prod': ProdConfig,
}