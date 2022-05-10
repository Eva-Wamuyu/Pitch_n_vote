from flask import Blueprint

app_bp = Blueprint('app_bp',__name__)

from . import views,errs