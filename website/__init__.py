# importing all stuffs which we need
# kerakli barcha modullarni import qilib olamiz

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

# some configuration our database
# database uchun kerakli config lar 
db = SQLAlchemy()

def createapp():
    #Initializing the app
    # app py faylini initializasiya qilamiz\

    app = Flask(__name__)
    app.config['SECRET_KEY']='hello'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    loginmanager = LoginManager(app)
    loginmanager.login_view = '/'

    # routelarni yaratib olamiz
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Users
    createdatabase(app)

    @loginmanager.user_loader
    def userloader(id):
        return Users.query.filter_by(id=int(id)).first()

    #Returning the app
    # app ni return qilamiz.
    return app

def createdatabase(app):
    if not path.exists("website/database.db"):
        db.create_all(app=app)
        print('Created')