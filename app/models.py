from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db,login_manager
from sqlalchemy import desc

class User(db.Model,UserMixin):
  __tablename__ = 'all_users'
  _id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  pass_pass = db.Column(db.String)
  posts = db.relationship('Post', backref='all_users',lazy='dynamic')
  comments = db.relationship('Comments', backref='all_users',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')


  @password.setter
  def password(self, password):
    self.pass_pass = generate_password_hash(password)
    print(self.pass_pass)

  def verify_password(self, password):
    return check_password_hash(self.pass_pass, password)

  def get_id(self):
      return self._id
  @login_manager.user_loader
  def load_user(user_id):
      return User.query.get(user_id)

  
      
class Post(db.Model):
  __tablename__='posts'
  _id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(80), nullable=False)
  content = db.Column(db.Text, nullable=False)
  votes = db.Column(db.Integer, nullable=False)
  author_id = db.Column(db.Integer,db.ForeignKey('all_users._id'))
  comments = db.relationship('Comments', backref='posts',lazy='dynamic')
  the_date = db.Column(db.DateTime)
  def get_posts():
     all_posts = Post.query.all()
     return all_posts
  def get_cat_posts(the_cat):
    the_spec = Post.query.filter_by(category=the_cat)
    return the_spec  
  def get_author(self,x):
    author = User.query.filter_by(_id=x).first()
    return author.username;
  
  def get_comments(self,y):
    arr_comm = Comments.query.filter_by(post=y).all()
   
    return arr_comm

 

class Comments(db.Model):
  __tablename__ = 'comments'
  _id = db.Column(db.Integer,primary_key=True)
  content = db.Column(db.Text,nullable=False)
  author = db.Column(db.Integer,db.ForeignKey('all_users._id'))
  post = db.Column(db.Integer,db.ForeignKey('posts._id'))
  the_date = db.Column(db.DateTime)


  def get_author(self,x):
    author = User.query.filter_by(_id=x).first()
    return author.username;
  def get_post(self,y):
    the_post = Post.query.filter_by(_id=y).first()
    return the_post.content;

  
  