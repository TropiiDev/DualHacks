from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # do stuff here
        pass
    return render_template("login.html")

@auth.route('/logout')
def pricing():
    return render_template("logout.html")

@auth.route('/signup')
def classes():
    return render_template('signup.html')