from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def home():
    return render_template("login.html")

@auth.route('/logout')
def pricing():
    return render_template("logout.html")

@auth.route('/signup')
def classes():
    return render_template('signup.html')