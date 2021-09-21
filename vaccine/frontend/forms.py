from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets.core import Select


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class ApplicationForm(FlaskForm):
    given_name = StringField('Given name', validators=[DataRequired()])
    family_name = StringField('Family name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
                         'Male', 'Female', 'Other', 'Unknown'])
    indigenous_status = SelectField('Indigenous Status', choices=[
                                    'Aboriginal but not Torres Strait Islander origin', ' Torres Strait Islander but not Aboriginal origin', 'Both Aboriginal & Torres Strait Islander origin', 'Neither Aboriginal nor Torres Strait Islander origin', 'Declined to Respond', 'Unknown'])
    age = IntegerField('Age', validators=[DataRequired()])
    place_of_birth = StringField('Place of Birth', validators=[DataRequired()])
    residential_address = StringField(
        'Current Living Address', validators=[DataRequired()])
    residence_status = SelectField('Residence Status', choices=[
        'Eligible Australian Resident', 'Ineligible Overseas Resident', 'Reciprocal Overseas Resident', 'Unknown'])
    medicare = SelectField('Do you have a medicare card?', choices=[
                           'Yes', 'No'])
    vaccine_history = SelectField('Have you previously get any COVID-19 vaccince?',
                                  choices=['Yes', 'No'])
    work_type = SelectField('Types of work that best applies to you', choices=[
                            'General public', 'Border workers', 'Carer', 'Correctional center', 'Frontline health care worker', 'Other health care workers', 'Quarantine facility workers'], )
    booker_description = StringField(
        'Description that best applies to you', validators=[DataRequired()])
    parking_required = SelectField('Accessibility Parking Required?',
                                   choices=['Yes', 'No'])
    interpreter_required = SelectField('Required an Interpreter?',
                                       choices=['Yes', 'No'])
    submit = SubmitField('Submit')


class ScheduleForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    state = SelectField('State', choices=['NSW'], validators=[DataRequired()])
    city = SelectField('City / Suburb', choices=[
                       'Darlinghurst', 'Sydney Olympic Park', 'Wollongong'], validators=[DataRequired()])
    vaccination_cite = SelectField('Vaccination Cite', choices=[
                                   'Darlinghurst: St. Vincents Hospital MASS Pfizer', 'Sydney Olympic Park: Qudos Bank Arena NSW Health Vaccination Centre', 'Wollongong: Wollongong Vaccination Clinic Pfizer'], validators=[DataRequired()])
    first_slot = SelectField('First Dose Slot', choices=[
                             '2021-11-1 09:45', '2021-11-1 10:00', '2021-11-1 10:15'], validators=[DataRequired()])
    second_slot = SelectField('Second Dose Slot', choices=[
                              '2021-11-25 10:45', '2021-11-25 11:00', '2021-11-25 11:15'], validators=[DataRequired()])
    medical_condition = StringField(
        'Please list any medical concerns or questions', validators=[DataRequired()])

    submit = SubmitField('Submit')
