from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, IntegerField, SubmitField, SelectField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from wtforms.widgets.core import Select


class AddressForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    address1 = StringField('Address1', validators=[DataRequired()])
    address2 = StringField('Address2', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=['Male', 'Female', 'Other', 'Unknown'], validators=[DataRequired()])
    # dob = StringField('Date of Birth', validators=[DataRequired()])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    licence_no = StringField('Licence Number', validators=[DataRequired()])
    address1 = StringField('Address 1', validators=[DataRequired()])
    address2 = StringField('Address 2 (Optional)')
    country = SelectField('Country', choices=['Australia'], validators=[DataRequired()])
    state = SelectField('State', choices=['ACT', 'NSW', 'VIC', 'SA', 'WA', 'NT', 'TAS'], validators=[DataRequired()])
    zipcode = IntegerField('Postcode', validators=[DataRequired()])
    # submit = SubmitField('Create Account')


class EditDetailsForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=['Male', 'Female', 'Other', 'Unknown'], validators=[DataRequired()])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    # dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    licence_no = StringField('Licence Number', validators=[DataRequired()])
    address1 = StringField('Address 1', validators=[DataRequired()])
    address2 = StringField('Address 2 (Optional)')
    country = SelectField('Country', choices=['Australia'], validators=[DataRequired()])
    state = SelectField('State', choices=['ACT', 'NSW', 'VIC', 'SA', 'WA', 'NT', 'TAS'], validators=[DataRequired()])
    zipcode = IntegerField('Postcode', validators=[DataRequired()])




