from operator import add
from flask import Blueprint, jsonify, request, make_response
from werkzeug.wrappers import response
from models import Address, db
from flask_login import login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

address_blueprint = Blueprint(
    'address_api_routes', __name__, url_prefix='/api/address')

user_blueprint = Blueprint('user_api_routes', __name__,
                           url_prefix='/api/user')


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


@user_blueprint.route('/all', methods=['GET'])
def get_all_users():
    all_user = Address.query.all()
    result = [user.serialize() for user in all_user]
    response = {
        # 'message': 'Returning all users',
        'result': result
    }
    return jsonify(response)


@user_blueprint.route('/create', methods=['POST'])
def create_user():
    try:
        user = Address()
        user.email = request.form["email"]
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.gender = request.form["gender"]
        user.dob = request.form["dob"]
        user.licence_no = request.form["licence_no"]
        user.address1 = request.form["address1"]
        user.address2 = request.form["address2"]
        user.country = request.form["country"]
        user.state = request.form["state"]
        user.zipcode = request.form["zipcode"]

        user.password = generate_password_hash(request.form['password'],
                                               method='sha256')

        user.is_admin = False
        db.session.add(user)
        db.session.commit()
        response = {'message': 'User Created', 'result': user.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message': 'Error in creating response'}
    return jsonify(response)


@user_blueprint.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = Address.query.filter_by(email=email).first()
    if not user:
        response = {'message': 'user does not exists'}
        return make_response(jsonify(response), 401)
    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        login_user(user)
        response = {'message': 'logged in ',
                    'api_key': user.api_key}
        return make_response(jsonify(response), 200)

    response = {'message': 'Access denied'}
    return make_response(jsonify(response), 401)


@user_blueprint.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'logged out'})
    return jsonify({'message': 'No user logged in'}), 401


@user_blueprint.route('/<email>/exists', methods=['GET'])
def user_exists(email):
    user = Address.query.filter_by(email=email).first()
    if user:
        return jsonify({"result": True}), 200

    return jsonify({"result": False}), 404


@user_blueprint.route('/', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({'result': current_user.serialize()}), 200
    else:
        return jsonify({'message': "User not logged in"}), 401


@user_blueprint.route("/<string:email>", methods=['GET'])
def current_user(email):
    user_info = Address.query.filter_by(email=email).first()
    return user_info.serialize()
