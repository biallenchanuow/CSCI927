from flask import Blueprint
from flask import render_template
from flask import request, make_response, jsonify
from flask import flash
from login.models import User
from login.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

blueprint = Blueprint('blueprint', __name__, url_prefix='/api/user')

# def home():
#     return render_template('index.html', user=current_user)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                response = {'message': 'logged in'}
                return make_response(jsonify(response), 200)
                # return redirect(url_for('views.check_points'))
            else:
                flash('Incorrect password, please try again', category='error')
                response = {'message': 'incorrect password'}
                return make_response(jsonify(response), 200)
        else:
            flash('Email does not exist', category='error')
            # response = {'message': 'incorrect email'}
            # return make_response(jsonify(response), 200)

    response = {'message': 'Access denied'}
    return make_response(jsonify(response), 401)
    # return render_template("checkpoints.html", user=current_user)


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
        # user.first_name = request.form["first_name"]
        # user.last_name = request.form["last_name"]
        # user.dob = request.form["dob"]
        # user.gender = request.form["gender"]
        # user.address1 = request.form["address1"]
        # user.address2 = request.form["address2"]
        # user.country = request.form["country"]
        # user.state = request.form["state"]
        # user.zipcode = request.form["zipcode"]
        # user.demerit = 0
        # user.licence_no = request.form["licence_no"]

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', category='success')
        # login_user(user, remember=True)
        # return redirect(url_for('views.check_points'))
        response = {'message':'User Created', 'result': user.serialize()}
        return jsonify(response)

    # return render_template("signup.html", user=current_user)


@blueprint.route('/<string:email>', methods=['GET', 'POST'])
def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user.serialize()


@blueprint.route('/edit-details', methods=['POST'])
def edit_details(id):
    user = User.query.get(id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.dob = request.form["dob"]
    user.gender = request.form["gender"]
    user.address1 = request.form["address1"]
    user.address2 = request.form["address2"]
    user.country = request.form["country"]
    user.state = request.form["state"]
    user.zipcode = request.form["zipcode"]
    user.demerit = 0
    user.licence_no = request.form["licence_no"]

    db.session.commit()
    flash('Details updated!', category='success')

    response = {'message': 'Details edited', 'result': user.serialize()}
    return jsonify(response)