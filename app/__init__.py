from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail

from config import config_options

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
mail = Mail()



#MAIN ENTRY OF THE APP
def create_app(config_filename):
    app = Flask(__name__)
    
    
    
    app.config.from_object(config_options[config_filename])
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from .main import app_bp
    app.register_blueprint(app_bp)
    
   


    
    return app



