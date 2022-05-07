from flask import Flask
from ..config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#MAIN ENTRY OF THE APP
def create_app(config_filename):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_filename])
    db.init_app(app)

    from .main import app_bp
    app.register_blueprint(app_bp)

    return app


create_app()
