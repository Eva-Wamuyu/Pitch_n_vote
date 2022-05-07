import os
class Config():
    SECRET_KEY = os.environ['SECRET_KEY']
    USER_NAME = os.environ['USER_NAME']
    DATABASE = os.environ['DATABASE']
    HOSTNAME = os.environ['HOSTNAME']








class DevConfig(Config):

  DEBUG = True


class ProdConfig(Config):
  pass

config_options = {
  'dev': DevConfig,
  'prod': ProdConfig,
}