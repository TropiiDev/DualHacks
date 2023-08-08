from flask import Blueprint, render_template, url_for
from flask_login import login_required
from flask import Blueprint, render_template, request
import json
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
    course_list = json.load(open(os.path.abspath('instance\courses.json')))
    print(course_list['Users'])
    return render_template('courses.html', course_list=course_list)

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

@views.route('/course')
def course():
    user = request.args['user'].replace('%20', ' ')
    name = request.args['name'].strip("'").replace('%20', ' ')
    print(user, name)
    try:
        course_ = json.load(open(os.path.abspath('instance\courses.json')))['Users'][user]["CoursesMade"][name]
    except KeyError:
        return "Invalid course. If this is a mistake, please contact a developer."
    texts= course_['Text'].split('\n')
    title = name
    return render_template('course.html', texts=texts, title=title, user=user)

@views.route('course_creation', methods=['GET', 'POST'])
def course_creation():
    if request.method == "POST":
        course_title = request.form.get('beans')
        course_main_text = request.form.get('moreBeans')

        if (course_title is not None) and (course_main_text is not None):
            current_courses = json.load(open(os.path.abspath('instance\courses.json')))
            try:
                if current_courses['Users'][current_user.username] is not None:
                    current_courses['Users'][current_user.username]['CoursesMade'][course_title] = {
                        "Text": course_main_text
                    }
            except KeyError:
                    current_courses['Users'][current_user.username] = {
                        "CoursesMade": {course_title: {"Text": course_main_text
                            }
                        }
                    }
            json.dump(current_courses, open(os.path.abspath('instance\courses.json'), 'w'), indent=4)

    return render_template('course_creation.html')