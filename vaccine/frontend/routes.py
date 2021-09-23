from flask import Blueprint, render_template, session, redirect, request, flash, url_for
from flask_login import current_user
from api.user_api import UserClient
from api.application_api import ApplicationClient
from api.schedule_api import ScheduleClient
import forms

blueprint = Blueprint('frontend', __name__)


@blueprint.route('/', methods=['GET'])
def frontpage():
    return render_template('index.html')


@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            if UserClient.user_exists(username):
                flash("Please try another user name")
                return render_template('register.html', form=form)
            else:
                user = UserClient.create_user(form)
                if user:
                    flash("Registered. Please login.")
                    return redirect(url_for('frontend.login'))
        else:
            flash("Errors")

    return render_template('register.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            api_key = UserClient.login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']
                flash("Login successed. Please fill the personal information form")
                return redirect(url_for('frontend.apply'))
            else:
                flash('Cannot Login')
        else:
            flash('Cannot Login')

    return render_template('login.html', form=form)


@blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('frontend.frontpage'))


@blueprint.route('/application', methods=['GET', 'POST'])
def apply():
    form = forms.ApplicationForm()
    if request.method == 'POST':
        # if 'user' not in session:
        #flash('Please login')
        # return redirect(url_for('frontend.login'))

        if form.validate_on_submit():
            given_name = form.given_name.data
            application = ApplicationClient.create_application(form)
            flash("Sumbitted. Please schedule your vaccination.")
            return redirect(url_for('frontend.schedule'))
        else:
            flash("Errors")

    return render_template('application.html', form=form)


@blueprint.route('/schedule', methods=['GET', 'POST'])
def schedule():
    form = forms.ScheduleForm()
    if request.method == 'POST':
        if 'user' not in session:
            flash('Please login')
            return redirect(url_for('frontend.login'))
        else:
            schedule = ScheduleClient.create_schedule(form)
            flash("Your appointment is submmited.")
            return redirect(url_for('frontend.thanks'))

    return render_template('schedule.html', form=form)


@blueprint.route('/thanks', methods=['GET'])
def thanks():
    if 'user' not in session:
        flash('Please login')
        return redirect(url_for('frontend.login'))

    return render_template('thankyou.html')
