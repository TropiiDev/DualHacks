from flask import Blueprint, render_template
from flask_login import login_required

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

@views.route('/enroll')
def enroll():
    return render_template('enroll.html')

@views.route('/exampleCourse')
def example_course():
    return render_template('exampleCourse.html')

@views.route('/user')
@login_required
def user_page():
    return render_template('user_page.html')

@views.route('/about')
def about():
    return render_template('about.html')