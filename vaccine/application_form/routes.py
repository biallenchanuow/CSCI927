from flask import Blueprint, request, jsonify
from werkzeug.wrappers import response
from models import Application, db


application_blueprint = Blueprint(
    'application_api_routes', __name__, url_prefix='/api/application')


@application_blueprint.route('/all', methods=['GET'])
def get_all_applications():
    all_applications = Application.query.all()
    result = [application.serialize() for application in all_applications]
    response = {'result': result}
    return jsonify(result)


@application_blueprint.route('/create', methods=['POST'])
def create_application():
    try:
        application = Application()
        application.given_name = request.form['given_name']
        application.family_name = request.form['family_name']
        application.gender = request.form['gender']
        application.indigenous_status = request.form['indigenous_status']
        application.age = request.form['age']
        application.place_of_birth = request.form['place_of_birth']
        application.residential_address = request.form['residential_address']
        application.residence_status = request.form['residence_status']
        application.medicare = request.form['medicare']
        application.vaccine_history = request.form['vaccine_history']
        application.work_type = request.form['work_type']
        application.booker_description = request.form['booker_description']
        application.parking_required = request.form['parking_required']
        application.interpreter_required = request.form['interpreter_required']

        db.session.add(application)
        db.session.commit()

        response = {'message': 'Application form created',
                    'result': application.serialize()}

    except Exception as e:
        print(str(e))
        response = {'message': 'Application create failed'}

    return jsonify(response)


@application_blueprint.route('/delete/<int:id>')
def delete(id):
    delete_application = Application.query.get_or_404(id)
    db.session.delete(delete_application)
    db.session.commit()
    return jsonify({'message': 'Application deleted'})
