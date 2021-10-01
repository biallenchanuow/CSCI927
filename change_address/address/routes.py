from operator import add
from flask import Blueprint, request, jsonify
from werkzeug.wrappers import response
from models import Address, db

address_blueprint = Blueprint(
    'address_api_routes', __name__, url_prefix='/api/address')


@address_blueprint.route('/update/<string:email>', methods=['POST'])
def update_address(email):
    try:
        address = Address()
        update_info = address.query.filter_by(email=email).first()
        update_info.address1 = request.form['address1']
        update_info.address2 = request.form['address2']
        update_info.country = request.form['country']
        update_info.state = request.form['state']
        update_info.zipcode = request.form['zipcode']

        db.session.commit()

        response = {'message': 'Address updated',
                    'result': update_info.serialize()}

    except Exception as e:
        print(str(e))
        response = {'message': 'Updated failed'}

    return jsonify(response)
