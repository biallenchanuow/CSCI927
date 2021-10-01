from flask import Blueprint, render_template, session, redirect, request, flash, url_for
# from flask_login import current_user
from api.address_api import AddressClient
import forms

blueprint = Blueprint('frontend', __name__)


@blueprint.route('/address', methods=['GET', 'POST'])
def address():
    form = forms.AddressForm()
    if request.method == 'POST':
        # if 'user' not in session:
        # flash('Please login')
        # return redirect(url_for('frontend.login'))

        if form.validate_on_submit():
            zipcode = form.zipcode.data
            address = AddressClient.update(form)
            flash("Update successful")
            # return redirect(url_for('frontend.address'))
        else:
            flash("Errors")

    return render_template('address.html', form=form)
