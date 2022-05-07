from flask import Flask
# from ..config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

#MAIN ENTRY OF THE APP
def create_app():
    app = Flask(__name__)

    
    
    # app.config.from_object(config_options[config_filename])
    db.init_app(app)
    bootstrap.init_app(app)
    from main import app_bp
    app.register_blueprint(app_bp)
    
    return app


create_app()
