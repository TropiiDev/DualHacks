from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)
from flask_login import login_user, login_required, logout_user, current_user

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
def user_page():
    return render_template('user_page.html')

@views.route('/about')
def about():
    return render_template('about.html', user=current_user)

@views.route('/setprofilepic')
def setprofilepic():
    current_user.profile_picture = request.headers.get('url')
    print(current_user.username)
    # print(f'{current_user.profile_picture}')
    return f'set to {current_user.profile_picture}'

@views.route('/getprofilepic')
def getprofilepic():
    print(current_user.username)
    print(current_user.profile_picture, 'sadness')
    return current_user.profile_picture