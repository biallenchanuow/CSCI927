from flask import Blueprint
from flask import render_template, request, jsonify
from checkpoints.models import UserDemerit, db

blueprint = Blueprint("blueprint", __name__, url_prefix="/api/checkpoints")


# @blueprint.route("/<int:id>", methods=['GET'])
# def get_demerit(id):
#     user_demerit = UserDemerit.query.get(id)
#     return user_demerit.serialize()


@blueprint.route("/update/<int:id>", methods=['POST'])
def update_demerit(id):
    user = UserDemerit.query.get(id)
    user.demerit = request.form['demerit']
    db.session.commit()
    response = {"message":"demerit updated"}
    return jsonify(response)


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
