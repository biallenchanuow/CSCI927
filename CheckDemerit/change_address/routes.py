from flask import Blueprint, session, json
from flask import render_template, request, jsonify
from change_address.models import UserAddress, db

blueprint = Blueprint("blueprint", __name__, url_prefix="/api/change-address")


@blueprint.route('/<string:email>', methods=['POST'])
def change_address(email):
    if request.method == 'POST':
        user = UserAddress.query.filter_by(email=email).first()
        user.address1 = request.form['address1']
        user.address2 = request.form['address2']
        user.country = request.form['country']
        user.state = request.form['state']
        user.zipcode = request.form['zipcode']

        # user = json.loads(request.data)
        # user.address1 = request.data['address1']
        # user.address2 = request.data['address2']
        # user.country = request.data['country']
        # user.state = request.data['state']
        # user.zipcode = request.data['zipcode']

        db.session.commit()
    response = {'message': 'address updated'}
    return jsonify(response)


@blueprint.route('/<email>', methods=['GET'])
def get_address_by_email(email):
    user = UserAddress.query.filter_by(email=email).first()
    return user.serialize()
