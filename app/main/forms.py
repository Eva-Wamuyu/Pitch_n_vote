from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField,ValidationError, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length,InputRequired
from ..models import User




class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Get In')
  
  

class SignupForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(),Email()])
  username = StringField('Username', validators=[DataRequired(),Length(min=3,message='username must be at least 3 characters')])
  password = PasswordField('Password', validators=[InputRequired(), EqualTo('password_two',message='Password must match')])
  password_two = PasswordField('Confirm Password', validators=[InputRequired()])
  submit = SubmitField('Sign Up')

  def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

  def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
  


class PostForm(FlaskForm):
  post = TextAreaField("What's in your mind?", validators=[DataRequired(), Length(min=15, message="Share a message longer than 15 characters")])
  category = RadioField("Category",choices=[("Tech","Technology"),("Agr","Agriculture"),("Edu","Education")], validators=[DataRequired()])
  submit = SubmitField('Share')


class Comment(FlaskForm):
  comment = TextAreaField("Remarks",validators=[DataRequired()])
  submit = SubmitField('Post')
