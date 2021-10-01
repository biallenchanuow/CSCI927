from flask import Blueprint
from flask import render_template, request, jsonify
from download.models import DemeritReport, db
import requests

blueprint = Blueprint("blueprint", __name__, url_prefix="/api/download")


@blueprint.route("/<int:id>", methods=['GET'])
def get_report(id):
    report = DemeritReport.query.get(id)
    return report.serialize()


@blueprint.route("/create", methods=['POST'])
def create_report():
    report = DemeritReport()
    report.id = request.form["id"]
    report.first_name = request.form["first_name"]
    report.last_name = request.form["last_name"]
    report.dob = request.form["dob"]
    report.licence_no = request.form["licence_no"]
    report.demerit = request.form["demerit"]
    report.address1 = request.form["address1"]
    report.address2 = request.form["address2"]
    report.state = request.form["state"]
    report.country = request.form["country"]
    report.zipcode = request.form['zipcode']

    db.session.add(report)
    db.session.commit()

    response = {'message': 'New report created'}
    return jsonify(response)

