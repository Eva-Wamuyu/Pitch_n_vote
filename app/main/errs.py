from flask import redirect, url_for,render_template
from . import app_bp

@app_bp.app_errorhandler(401)
def forbidden(e):
 
  return redirect(url_for('app_bp.login')),401
  


@app_bp.app_errorhandler(404)
def missing(e):
  return render_template("notfound.html")
  