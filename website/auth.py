from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET","POST"])
def login():



  return render_template("login.html", name="Hey there", cond=True)

@auth.route('/logout')
def logout():
  return "<p>logout</p>"

@auth.route('/signup', methods=["GET","POST"])
def signup():
  data = request.form
  if request.method == "POST":
    email = data.get("email")
    firstName = data.get("firstName")
    password1 = data.get("password1")
    password2 = data.get("password2")

    if len(email) < 4:
      flash('Email must be greater than 3 characters.', category="error")
    elif len(firstName) < 2:
      flash('First name must be greater than 1 character', category="error")
    elif password1 != password2:
      flash("Passwords don't match", category="error")
    elif len(password1) < 7:
      flash("Password must be atleast 7 characters.", category="error")
  return render_template("signup.html")