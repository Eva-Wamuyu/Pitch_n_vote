from flask import render_template,redirect,url_for, request,flash
from .forms import *
from flask_login import login_required,login_user, logout_user,current_user
from ..models import *
from . import app_bp
from .. import db
from ..mail import mail_message
from datetime import date



@app_bp.route('/')
def index():
  title = "Home|PnV"
  header = "All Categories"
  all_posts = Post.get_posts()
  
 
  return render_template("index.html",title=title,all_posts=all_posts,header=header)



@app_bp.route('/login',methods=['GET','POST'])
def login():
  title = "PnV|SignUp"
  form_title = "Login"
  form = LoginForm()
  if current_user.is_authenticated:
      return redirect(url_for('.profile',user=current_user))
 
  if form.validate_on_submit():
    user = User.query.filter_by(username= form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      person = form.username.data

      return redirect(url_for('.profile',user=person))
    flash('Username or Password not Valid')
  return render_template("login.html",form=form,title=title, form_title=form_title)


@app_bp.route('/signup', methods=["GET","POST"])
def signUp():
  title = "PnV|Login"
  form = SignupForm()
  form_title = "Create Account"
  

  if form.validate_on_submit():
    user = User(email=form.email.data, username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()

    mail_message("Welcome","mail/welcome",user.email,user=user)
    return redirect(url_for('.login',user=user.username))
  return render_template('signup.html',form=form,title=title, form_title=form_title)   


@app_bp.route('/profile/<user>', methods=["GET","POST"])
@login_required
def profile(user):
  
  form = PostForm()
  all_posts = Post.query.filter_by(author_id = current_user._id)
  title = "Profile"
  if form.validate_on_submit():
    post = Post(category=form.category.data, content=form.post.data, votes=0,author_id=current_user._id,the_date=date.today())
    db.session.add(post)
    db.session.commit()
    redirect (url_for('.profile',user=current_user.username))
  return render_template('profile.html',title=title, form=form, posts=all_posts,user=current_user.username)




@app_bp.route('/comment/<post>', methods=["GET","POST"])
@login_required
def post_comment(post):
  poster = current_user._id
  post_spec = Post.query.filter_by(_id=post).first()
  form = Comment()
  if form.validate_on_submit():
    new_comment = Comments(author=poster,content=form.comment.data,post=post,the_date=date.today())
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('.index'))

  return render_template("comment.html",form=form,post_spec=post_spec)

@app_bp.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('.index'))


@app_bp.route('/posts/tech')
def tech():
  title = 'Technology'
  header = title
  posts  = Post.get_cat_posts('Tech')
  

  return render_template('index.html',title=title,all_posts=posts,header=header)

@app_bp.route('/posts/agri')
def agric():
  title = 'Agriculture'
  header = title
  posts = Post.get_cat_posts('Agr')

  return render_template('index.html',title=title,all_posts=posts,header=header)

@app_bp.route('/posts/edu')
def edu():
  title = 'Education'
  header = title
  posts = Post.get_cat_posts('Edu')
  return render_template('index.html',title=title,all_posts=posts,header=header)

@app_bp.route('/not-found')
def lost():
  title = '404'
 
  return render_template('notfound.html',title=title)


@app_bp.route('/vote/<post>')
@login_required
def vote(post):
  post_spec = Post.query.filter_by(_id=post).first()

  return render_template("index.html")
  

@app_bp.route('/vote/<post>')
@login_required
def dvote(post):
  post_spec = Post.query.filter_by(_id=post).first()
  post_spec['votes'] = post_spec['votes'] -1;
# @app_bp.route("/comments/<a_post>")
# def get_comments():
#   title = "PnV|Comments"
#   return render_template("comments.html",title=title)