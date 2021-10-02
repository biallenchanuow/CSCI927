from flask import Blueprint, render_template, session, redirect, request, flash, url_for
# from flask_login import current_user
from api.address_api import AddressClient, UserClient
import forms
import requests

blueprint = Blueprint('frontend', __name__)


@blueprint.route('/', methods=['GET'])
def frontpage():
    return render_template('index.html')


@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data

            if UserClient.user_exists(email):
                flash("Please try another email address")
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
                flash("Login successed")
                return redirect(url_for('frontend.address'))
            else:
                flash('Cannot Login')
        else:
            flash('Cannot Login')

    return render_template('login.html', form=form)


@blueprint.route('/address', methods=['GET', 'POST'])
def address():
    if 'user' not in session:
        flash('Please login')
        return redirect(url_for('frontend.login'))
    else:
        email = session['user']['email']
        form = forms.AddressForm()
        if request.method == 'GET':
            url = 'http://127.0.0.1:3001/' + f'/api/user/{email}'
            current_user = requests.get(url).json()

            first_name = current_user['first_name']
            last_name = current_user['last_name']
            gender = current_user['gender']
            dob = current_user['dob']
            email = current_user['email']
            licence_no = current_user['licence_no']
            return render_template('address.html', first_name=first_name, last_name=last_name, gender=gender, dob=dob, email=email, licence_no=licence_no, form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                zipcode = form.zipcode.data
                address = AddressClient.update(form)
                flash("Update successful")
                return redirect(url_for('frontend.thanks'))
            else:
                flash("Errors")
                return render_template('address.html', form=form)
    return render_template('address.html', form=form)


@blueprint.route('/thanks', methods=['GET'])
def thanks():
    if 'user' not in session:
        flash('Please login')
        return redirect(url_for('frontend.login'))

    return render_template('thankyou.html')


@blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('frontend.frontpage'))
