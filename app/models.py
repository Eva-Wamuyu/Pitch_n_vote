import email
from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
  __tablename__ = 'all_users'
  _id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), Unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

class Post(db.Model):
  __tablename__='posts'
  category = db.Column(db.String(80), nullable=False)
  content = db.Column(db.Text, nullable=False)
  the_date = db.Column(db.DateTime, nullable=False)
  votes = db.Column(db.Integer, nullable=False)
  comments = db.relationship('Comments', backref=db.backref('posts',lazy='True'))