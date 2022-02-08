# this file makes the website folder a python package
# allows to import website folder as a package. While importing __init__.py will run and the code will be
# available

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "BALAMURUGAN07" #encrypt the cookie and session data
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")
  from .models import User, Note
  
  create_database(app)
  loginManager = LoginManager()
  loginManager.login_view = "auth.login"
  loginManager.init_app(app)

  @loginManager.user_loader
  def loadUser(id):
    return User.query.get(int(id))
  
  return app

def create_database(app):
  if not path.exists('website/'+DB_NAME):
    db.create_all(app=app)
    print('Created Database!')
