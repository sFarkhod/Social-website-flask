# kerakli barcha modullarni import qilib olamiz
# from os import link
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Posts, Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import db

views = Blueprint("views", __name__)

# har bir sessiya (page) uchun alohida route yaratamiz 
@views.route('/')
def mainroute():
    return "<h1>Hello world"

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                print('Logged in')
                return redirect(url_for('views.posts'))
            else:
                print('Wrong password')
        else:
            print('Username does not exist')
    return render_template("login.html")



@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        username_exists = Users.query.filter_by(username=username).first()
        email_exists = Users.query.filter_by(email=email).first()
        if password1 != password2:
            print('Passwords don\'t match')
        elif username_exists or email_exists:
            print('User already exists')
        elif len(password1) < 6 or len(username) < 6:
            print('Length of username or password is too short')
        else:
            new_user = Users(username=username, email=email, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('views.posts'))
    return render_template("register.html")


@views.route('/posts')
@login_required
def posts():
    posts = Posts.query.all()
    return render_template('posts.html', posts=posts[::-1])

@login_required
@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.mainroute'))


# ////////////////////////////////////////////////////////////////////////////////

# for posts

@views.route('create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        link = request.form.get('link')
        desc = request.form.get('desc')
        data = Posts(by=current_user.username, link=link, desc=desc)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('views.posts'))
    return render_template('createpost.html')
