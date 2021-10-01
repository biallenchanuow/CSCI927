from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash, session
from flask import redirect, url_for
from flask_login import login_user, login_required, current_user
from frontend.api.user_api import UserAPI, USER_API_URL
import requests

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html', user=current_user)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = UserAPI.get_user(email)

        if email == user['email']:
            if password == user['password']:
                flash("Logged in successfully!", category='success')
                return redirect(url_for('frontend.check_points'))
            else:
                flash('Incorrect password, please try again', category='error')
        else:
            flash('Incorrect email, please try again', category='error')

    return render_template("login.html")


@blueprint.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('blueprint.home'))


@blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # first_name = request.form.get('first_name')
        # last_name = request.form.get('last_name')
        # gender = request.form.get('gender')
        # dob = request.form.get('dob')
        # licence_no = request.form.get('licence_no')
        # address1 = request.form.get('address1')
        # address2 = request.form.get('address2')
        # country = request.form.get('country')
        # state = request.form.get('state')
        # zipcode = request.form.get('zipcode')

        data = {
            'email': email,
            'password': password
            # 'first_name': first_name,
            # 'last_name': last_name,
            # 'gender': gender,
            # 'dob': dob,
            # 'licence_no': licence_no,
            # 'address1': address1,
            # 'address2': address2,
            # 'country': country,
            # 'state': state,
            # 'zipcode': zipcode
        }

        response = requests.get(USER_API_URL + f'/api/user/{email}')
        # user = requests.request(method='GET', url=url)

        if response.status_code == 200:
            flash('Email already exists.', category='error')

        else:
            user = UserAPI.create_user(data)
            flash('Account created successfully!', category='success')
            # login_user(user, remember=True)
            session['email'] = request.form['email']
            session['password'] = request.form['password']
            return redirect(url_for('blueprint.edit_details'))

    return render_template("signup.html")


@blueprint.route('/edit-details', methods=['GET', 'POST'])
def edit_details():
    if request.method == 'POST':
        email = session['email']
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        licence_no = request.form.get('licence_no')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        country = request.form.get('country')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'gender': gender,
            'dob': dob,
            'licence_no': licence_no,
            'address1': address1,
            'address2': address2,
            'country': country,
            'state': state,
            'zipcode': zipcode
        }

        user = UserAPI.edit_details(email, data)
        flash('Details added successfully!', category='success')
        return redirect(url_for('blueprint.home'))

    return render_template('edit-details.html')


def check_points():
    return render_template('check-points.html')


def download_report():
    pass


def change_address():
    pass