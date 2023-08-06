from flask import Blueprint, render_template, url_for
from flask_login import login_required
from flask import Blueprint, render_template, request
import os

views = Blueprint('views', __name__)
from flask_login import login_user, login_required, logout_user, current_user

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/pricing')
def pricing():
    return render_template("pricing.html")

@views.route('/classes')
@login_required
def classes():
    return render_template('classes.html')

@views.route('courses')
@login_required
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
    # loop through static/uploads and find the file that matches the current user's username
    # if the file exists, set the profile picture to that file
    # else, set the profile picture to the default which is empty_pfp.jpg
    for file in os.listdir('website/static/uploads'):
        if file == current_user.username + '.jpg':
            current_user.profile_picture = url_for('static', filename='uploads/' + current_user.username + '.jpg')
        else:
            current_user.profile_picture = url_for('static', filename='uploads/empty_pfp.jpg')
    return render_template('user_page.html', pfp=current_user.profile_picture, user=current_user)

@views.route('/about')
def about():
    return render_template('about.html', user=current_user)