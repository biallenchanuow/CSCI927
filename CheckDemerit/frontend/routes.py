from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash, session
from flask import redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login
from flask_login import login_user, login_required, current_user
from api.user_api import UserAPI, USER_API_URL
from api import CHECKPOINTS_API_URL
import requests
import wtforms, flask_wtf, forms

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' not in session:
        form = forms.LoginForm()
        if request.method == 'POST':
            url = USER_API_URL + '/api/user/' + form.email.data
            user = requests.get(url)

            if user:
                if check_password_hash(user.json()['password'], form.password.data):
                    # login_user(user, remember=True)
                    session['user'] = user.json()
                    session['licence_no'] = user.json()['licence_no']
                    flash('Log in successful! Please check the demerit points', category='success')
                    return redirect(url_for('blueprint.check_points'))
                else:
                    flash('Incorrect password', category='error')
            else:
                flash('User does not exist', category='error')
        return render_template('login.html', form=form)
    else:
        flash("You are already logged in.", category='success')
        return redirect(url_for('blueprint.check_points'))


@blueprint.route('/logout')
def logout():
    if 'user' in session:
        session.clear()
        flash('Logged out')
        return redirect(url_for('blueprint.login'))
    else:
        flash('You are not logged in', category='error')


@blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = forms.RegistrationForm()
    if request.method == 'POST':
        data = {
            'email': form.email.data,
            'password': form.password.data,
            'first_name':  form.first_name.data,
            'last_name': form.last_name.data,
            'gender': form.gender.data,
            'dob': form.dob.data,
            'licence_no': form.licence_no.data,
            'address1': form.address1.data,
            'address2': form.address2.data,
            'country': form.country.data,
            'state': form.state.data,
            'zipcode': form.zipcode.data
        }

        response = requests.get(USER_API_URL + f'/api/user/{form.email.data}')

        if response.status_code == 200:
            flash('Email already exists.', category='error')

        else:
            user = UserAPI.create_user(data)
            user_demerit = UserAPI.user_demerit_fetch(data)

            url = USER_API_URL + '/api/user/' + form.email.data
            user_session = requests.get(url)
            session['user'] = user_session.json()
            session['licence_no'] = user_session.json()['licence_no']

            flash('Account created successfully!', category='success')
            return redirect(url_for(f'blueprint.home'))

    return render_template("signup.html", form=form)


@blueprint.route('/edit-details', methods=['GET', 'POST'])
def edit_details():
    form = forms.EditDetailsForm()
    if request.method == 'POST':
        email = form.email.data

        data = {
            'first_name':  form.first_name.data,
            'last_name': form.last_name.data,
            'gender': form.gender.data,
            'dob': form.dob.data,
            'licence_no': form.licence_no.data,
            'address1': form.address1.data,
            'address2': form.address2.data,
            'country': form.country.data,
            'state': form.state.data,
            'zipcode': form.zipcode.data
        }

        user = UserAPI.edit_details(email, data)
        flash('Details added successfully!', category='success')
        return redirect(url_for('blueprint.home'))

    return render_template('edit-details.html', form=form)


@blueprint.route('/check-points', methods=['GET', 'POST'])
def check_points():
    if request.method == 'GET':
        if 'licence_no' not in session:
            flash('Please login')
            return redirect(url_for('blueprint.login'))

        licence_no = session['licence_no']
        url = CHECKPOINTS_API_URL + f'/api/checkpoints/{licence_no}'
        user = requests.get(url)

        user_demerit = user.json()['demerit']
        full_name = user.json()['full_name']
        dob = user.json()['dob']
        address = user.json()['address']
        download_url = '/download'
        return render_template('check-points.html', user_demerit=user_demerit, full_name=full_name, licence_no=licence_no, dob=dob, address=address, download_url=download_url)
    return render_template('check-points.html')


@blueprint.route('/check-points/download', methods=['GET', 'POST'])
def download_report():
    if request.method == 'GET':
        if 'licence_no' not in session:
            flash('Please login')
            return redirect(url_for('blueprint.login'))
        licence_no = session['licence_no']
        url = CHECKPOINTS_API_URL + f'/api/checkpoints/{licence_no}'
        user = requests.get(url)
        user_demerit = user.json()['demerit']
        full_name = user.json()['full_name']
        dob = user.json()['dob']
        address = user.json()['address']
        return render_template('download.html', user_demerit=user_demerit, full_name=full_name,
                               licence_no=licence_no, dob=dob, address=address)
    return render_template('download.html')






