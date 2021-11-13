from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()

def createapp():
    #Initializing the app
    app = Flask(__name__)
    app.config['SECRET_KEY']='hello'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    loginmanager = LoginManager(app)
    loginmanager.login_view = '/'

    #Making the routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Users
    createdatabase(app)

    @loginmanager.user_loader
    def userloader(id):
        return Users.query.filter_by(id=int(id)).first()

    #Returning the app
    return app

def createdatabase(app):
    if not path.exists("website/database.db"):
        db.create_all(app=app)
        print('Created')