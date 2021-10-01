from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets.core import Select


class AddressForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    address1 = StringField('Address 1', validators=[DataRequired()])
    address2 = StringField('Address 2 (Optional)')
    country = StringField('Country', validators=[DataRequired()])
    state = SelectField('State', choices=['NSW'], validators=[DataRequired()])
    zipcode = IntegerField('Postcode', validators=[DataRequired()])
    submit = SubmitField('Update Information')
