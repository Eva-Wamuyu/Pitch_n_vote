from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
  pass

class SignupForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  username = StringField('Username', validators=[DataRequired()])
  password = StringField('Password', validators=[DataRequired()])
  password2 = StringField('Confirm Password', validators=[DataRequired()])
  submit = SubmitField('Sign Up')
