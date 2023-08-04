from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/pricing')
def pricing():
    return render_template("pricing.html")

@views.route('/classes')
def classes():
    return render_template('classes.html')

@views.route('courses')
def courses():
    return render_template('courses.html')