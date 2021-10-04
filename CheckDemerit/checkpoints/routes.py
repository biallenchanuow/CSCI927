from flask import Blueprint
from flask import render_template, request, jsonify, flash
import requests
from models import UserDemerit, db
# from frontend.api import USER_API_URL

blueprint = Blueprint("blueprint", __name__, url_prefix="/api/checkpoints")


# @blueprint.route("/<int:id>", methods=['GET'])
# def get_demerit(id):
#     user_demerit = UserDemerit.query.get(id)
#     return user_demerit.serialize()

USER_API_URL = 'http://user-server-checkpoints-b:4001'
CHECKPOINTS_API_URL = 'http://checkpoints-server-b:4002'


@blueprint.route("/update/<email>", methods=['POST'])
def update_demerit(email):
    user = UserDemerit.query.filter_by(email=email).first()
    user.demerit = request.form['demerit']

    response = {"message": "demerit updated"}
    demerit_fetch(USER_API_URL + '/api/user', user.email, user.demerit)
    db.session.commit()
    return jsonify(response)


@blueprint.route("/update/fetch", methods=['POST'])
def demerit_fetch(api_url, user_email, demerit):
    url = api_url + '/update-demerit/' + user_email + '&' + str(demerit)
    response = requests.post(url=url)
    updated_information = {}
    if response:
        return response
    return updated_information


@blueprint.route("/add", methods=['POST'])
def add_demerit():
    user_demerit = UserDemerit()
    user_demerit.id = request.form["id"]
    user_demerit.first_name = request.form["first_name"]
    user_demerit.last_name = request.form["last_name"]
    user_demerit.dob = request.form["dob"]
    user_demerit.licence_no = request.form["licence_no"]
    user_demerit.demerit = request.form["demerit"]
    user_demerit.address1 = request.form["address1"]
    user_demerit.address2 = request.form["address2"]
    user_demerit.state = request.form["state"]
    user_demerit.country = request.form["country"]
    user_demerit.zipcode = request.form['zipcode']

    db.session.add(user_demerit)
    db.session.commit()

    response = {'message': 'New report created'}
    return jsonify(response)


@blueprint.route("/<string:licence_no>", methods=['GET'])
def get_demerit_by_licence(licence_no):
    user_demerit = UserDemerit.query.filter_by(licence_no=licence_no).first()
    return user_demerit.serialize()


@blueprint.route('/user-fetch', methods=['GET', 'POST'])
def user_fetch():
    if request.method == 'POST':
        user = UserDemerit()
        user.email = request.form["email"]
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