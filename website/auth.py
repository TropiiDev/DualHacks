from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/login')
def home():
    return render_template("login.html")

@views.route('/logout')
def pricing():
    return render_template("logout.html")

@views.route('/signup')
def classes():
    return render_template('signup.html')