from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db,login_manager

class User(db.Model,UserMixin):
  __tablename__ = 'all_users'
  _id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  pass_pass = db.Column(db.String)
  posts = db.relationship('Post', backref=db.backref('all_users',lazy='dynamic'))
  comments = db.relationship('Comment', backref=db.backref('comments',lazy='dynamic'))

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')


  @password.setter
  def password(self, password):
    self.pass_pass = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_pass, password)

  @login_manager.user_loader
  def load_user( user_id):
      return User.query.get(int(user_id))
      
class Post(db.Model):
  __tablename__='posts'
  _id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(80), nullable=False)
  content = db.Column(db.Text, nullable=False)
  the_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  votes = db.Column(db.Integer, nullable=False)
  author_id = db.Column(db.Integer,db.ForeignKey('all_users._id'))
  comments = db.relationship('Comments', backref=db.backref('posts',lazy='True'))


class Comments(db.Model):
  __tablename__ = 'comments'
  _id = db.Column(db.Integer,primary_key=True)
  comment_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  author = db.relationship(db.Integer,db.ForeignKey('all_users._id'))
  post = db.relationship(db.Integer,db.ForeignKey('posts._id'))
