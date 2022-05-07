from . import app_bp
from flask import render_template
from .forms import *


@app_bp.route('/')
def index():
  title = "Home|PnV"
  return render_template("index.html")

@app_bp.route('/signup',methods=['GET','POST'])
def signup():
  title = "PnV|SignUp"
  form = SignupForm()

  return render_template("signup.html",form=form)