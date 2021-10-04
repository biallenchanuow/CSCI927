from flask_wtf import FlaskForm
from flask import session
from flask_login import current_user
from wtforms import StringField, PasswordField, HiddenField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets.core import Select
from api.address_api import AddressClient, UserClient


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
                         'Male', 'Female', 'Other', 'Unknown'])
    dob = StringField("Date of birth (yyyy-mm-dd)",
                      validators=[DataRequired()])
    licence_no = StringField("Licence No.", validators=[DataRequired()])
    address1 = StringField('Address 1', validators=[DataRequired()])
    address2 = StringField('Address 2 (Optional)')
    country = StringField('Country', validators=[DataRequired()])
    state = SelectField('State', choices=['NSW'], validators=[DataRequired()])
    zipcode = IntegerField('Postcode', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class AddressForm(FlaskForm):
    #email = StringField('Email', render_kw={'readonly': True})
    #first_name = StringField("First name", render_kw={'readonly': True})
    #last_name = StringField("Last name", render_kw={'readonly': True})
    # gender = SelectField('Gender', choices=[
    # 'Male', 'Female', 'Other', 'Unknown'], render_kw=#{'readonly': True})
    # dob = StringField("Date of birth (yyyy-mm-dd)",
    # render_kw={'readonly': True})
    #licence_no = StringField("Licence No.", render_kw={'readonly': True})
    address1 = StringField('Address 1', validators=[DataRequired()])
    address2 = StringField('Address 2 (Optional)')
    country = StringField('Country', validators=[DataRequired()])
    state = SelectField('State', choices=['NSW'], validators=[DataRequired()])
    zipcode = IntegerField('Postcode', validators=[DataRequired()])
    submit = SubmitField('Update Information')
