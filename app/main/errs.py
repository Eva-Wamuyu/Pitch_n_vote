from flask import redirect, url_for,render_template
from . import app_bp
from .forms import LoginForm
@app_bp.app_errorhandler(401)
def forbidden(e):
  form = LoginForm();
  
  return render_template('login.html',form=form,title="Login",form_title="You need to log in inorder to comment"),401


@app_bp.app_errorhandler(404)
def missing(e):
  return render_template("notfound.html")
  