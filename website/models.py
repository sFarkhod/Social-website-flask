from datetime import datetime, time
# from os import link
from . import db
from flask_login import UserMixin

# User klasi databaseda kerakli infolarni saqlaydi. Va keyinchalik views da routalar ichida ishlatamiz.
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))


# post cllasi. 
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    by = db.Column(db.String(100))
    link = db.Column(db.String(900))
    desc = db.Column(db.String(200))  # agar description uchun so'zlar uzunligi kam bo'lsa uzaytiramiz.
    date = db.Column(db.DateTime, default=datetime.now())


# messagelar uchun yangi class
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(10))
    by = db.Column(db.String(10))
    to = db.Column(db.String(10))
    message = db.Column(db.String(500))
    time = db.Column(db.DateTime, default=datetime.now())

