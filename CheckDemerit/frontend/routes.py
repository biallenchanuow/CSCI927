from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash, session
from flask import redirect, url_for
import flask_login
from flask_login import login_user, login_required, current_user
from frontend.api.user_api import UserAPI, USER_API_URL
from frontend.api.checkpoints_api import CheckPointsAPI, CHECKPOINTS_API_URL
from frontend.api import CHANGEADDRESS_API_URL
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
                # user = UserAPI.get_user(email)
                email = request.form['email']
                session['email'] = email
                # login_user()
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
            'password': password,
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
            # session['email'] = request.form['email']
            # session['password'] = request.form['password']
            return redirect(url_for(f'blueprint.login'))

    return render_template("signup.html")


@blueprint.route('/edit-details', methods=['GET', 'POST'])
def edit_details():
    if request.method == 'POST':
        # user = flask_login.current_user
        # email = user.email
        # email = session['email']
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


@blueprint.route('/enter-licence', methods=['GET', 'POST'])
def enter_licence():
    if request.method == 'POST':
        licence_no = request.form['licence_no']
        # user_demerit = CheckPointsAPI.show_demerit(licence_no)
        # demerit = user_demerit.demerit
        return redirect(url_for('blueprint.check_points', licence_no=licence_no))
        # else:
        #     flash("Invalid licence number. Please try again.", category="wrong")

    return render_template('enter-licence.html')


@blueprint.route('/check-points/<licence_no>', methods=['GET', 'POST'])
def check_points(licence_no):
    if request.method == 'GET':
        url = CHECKPOINTS_API_URL + f'/api/checkpoints/{licence_no}'
        user = requests.get(url)

        user_demerit = user.json()['demerit']
        full_name = user.json()['full_name']
        dob = user.json()['dob']
        address = user.json()['address']
        download_url = f'/download/{licence_no}'
        return render_template('check-points.html', user_demerit=user_demerit, full_name=full_name, licence_no=licence_no, dob=dob, address=address, download_url=download_url)
    return render_template('check-points.html')


@blueprint.route('/check-points/download/<licence_no>', methods=['GET', 'POST'])
def download_report(licence_no):
    if request.method == 'GET':
        url = CHECKPOINTS_API_URL + f'/api/checkpoints/{licence_no}'
        user = requests.get(url)
        user_demerit = user.json()['demerit']
        full_name = user.json()['full_name']
        dob = user.json()['dob']
        address = user.json()['address']
        return render_template('download.html', user_demerit=user_demerit, full_name=full_name,
                               licence_no=licence_no, dob=dob, address=address)
    return render_template('download.html')


@blueprint.route('/change-address', methods=['GET', 'POST', 'PUT'])
def change_address():
    if request.method == 'POST' or request.method == 'PUT':
        email = request.form.get('email')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        country = request.form.get('country')
        state = request.form.get('state')
        zip = request.form.get('zip')

        data = {
            'address1': address1,
            'address2': address2,
            'country': country,
            'state': state,
            'zip': zip
        }

        url = CHANGEADDRESS_API_URL + f'/api/change-address/{email}'
        response = requests.post(url, data=data)

        if response:
            return redirect(url_for('blueprint.home'))
        else:
            flash("Update unsuccessful")

    return render_template('change-address.html')


# @blueprint.route('/change-address', methods=['GET', 'POST'])
# def change_address():
#     if request.method == 'POST':
#         if 'user' in session:
#             user = session['user']
#             email = user.email
#             address1 = request.form.get('address1')
#             address2 = request.form.get('address2')
#             country = request.form.get('country')
#             state = request.form.get('state')
#             zip = request.form.get('zip')
#
#             data = {
#                 'address1': address1,
#                 'address2': address2,
#                 'country': country,
#                 'state': state,
#                 'zip': zip
#             }
#
#             url = CHANGEADDRESS_API_URL + f'/api/change-address/{email}'
#             response = requests.request("POST", url=url, data=data)
#             if response:
#                 return render_template(url_for('blueprint.home'))
#
#             return render_template('change-address.html', user=user)
#         else:
#             flash('Please login first', category='loggedout')
#             return render_template(url_for('blueprint.login'))
#     return render_template('change-address.html')
