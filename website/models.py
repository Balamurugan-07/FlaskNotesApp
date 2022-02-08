from . import db # dot (.) means importing from current package. db is in __init__.py
from sqlalchemy.sql import func
from flask_login import UserMixin

# The user and the note table are in one to many relationship
class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# this class is a model for User table
class User(db.Model, UserMixin): #inherits db.Model
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  notes = db.relationship('Note') # everytime a note is created, the note id will add into this list.
  

