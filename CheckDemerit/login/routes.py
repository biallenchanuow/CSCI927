from flask import Blueprint
from flask import render_template
from flask import request, make_response, jsonify
from flask import flash
from models import User
from models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

blueprint = Blueprint('blueprint', __name__, url_prefix='/api/user')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            response = {'message': 'user does not exist'}
            return make_response(jsonify(response), 401)
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            response = {'message': 'logged in'}
            return make_response(jsonify(response), 200)


@blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'logged out'})
    return jsonify({'message':'not logged in'}), 401


@blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user = User()
        user.email = request.form["email"]
        user.password = generate_password_hash(request.form['password'], method='sha256')
        user.demerit = 0
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.dob = request.form["dob"]
        user.gender = request.form["gender"]
        user.licence_no = request.form["licence_no"]
        user.address1 = request.form["address1"]
        user.address2 = request.form["address2"]
        user.country = request.form["country"]
        user.state = request.form["state"]
        user.zipcode = request.form["zipcode"]

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', category='success')
        response = {'message':'User Created', 'result': user.serialize()}
        return jsonify(response)


@blueprint.route('/<string:email>', methods=['GET'])
def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user.serialize()


@blueprint.route('/get-user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id).first()
    return user.serialize()


@blueprint.route('/edit-details/<string:email>', methods=['POST'])
def edit_details(email):
    response = {}
    if request.method == 'POST':
        user = User.query.filter_by(email=email).first()
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.dob = request.form["dob"]
        user.gender = request.form["gender"]
        user.address1 = request.form["address1"]
        user.address2 = request.form["address2"]
        user.country = request.form["country"]
        user.state = request.form["state"]
        user.zipcode = request.form["zipcode"]
        user.licence_no = request.form["licence_no"]

        db.session.commit()
        flash('Details updated!', category='success')
        response = {'message': 'Details edited', 'result': user.serialize()}
    return jsonify(response)


@blueprint.route("/update-demerit/<string:email>&<string:demerit>", methods=['POST'])
def update_demerit_fetch(email, demerit):
    user = User.query.filter_by(email=email).first()
    user.demerit = int(demerit)
    db.session.commit()
    response = {"message":"demerit updated"}
    return jsonify(response)