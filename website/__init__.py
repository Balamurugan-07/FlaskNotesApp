# this file makes the website folder a python package
# allows to import website folder as a package. While importing __init__.py will run and the code will be
# available

from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "BALAMURUGAN07" #encrypt the cookie and session data
  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")
  return app

