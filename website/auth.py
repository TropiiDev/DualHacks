from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():  # login
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user is not None:
            if user.password:
                check_pass = check_password_hash(pwhash=user.password, password=password)
                print(user.profile_picture, 'profile')
                if check_pass:
                    flash('Logged in')
                    login_user(user=user, remember=True)
                else:
                    flash('Incorrect username or password!')
            pass
        else:
            flash('Incorrect username or password!')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('validationCustomUsername')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            new_user.profile_picture = '../empty_pfp.jpg'
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_pass():
    if request.method == "POST":
        flash("Password reset link sent to your email.", category="success")
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        email_address = "codebluical@gmail.com"
        email_password = "BluicalCodeTest55"

        # create email
        msg = EmailMessage()
        msg['Subject'] = "Reset your password!"
        msg['From'] = email_address
        msg['To'] = user.email
        msg.set_content("Click the link below to reset your password.\n\n" + "http://127.0.0.1:5000/reset/" + user.username + "/" + user.email)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user=email_address, password=email_password)
            smtp.send_message(msg)

    return render_template("resetpass.html")