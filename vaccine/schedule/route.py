from flask import Blueprint, request, jsonify
from werkzeug.wrappers import response
from model import Schedule, db


schedule_blueprint = Blueprint(
    'schedual_api_routes', __name__, url_prefix='/api/schedule')


@schedule_blueprint.route('/all', methods=['GET'])
def get_all_schedule():
    all_schedule = Schedule.query.all()
    result = [schedule.serialize() for schedule in all_schedule]
    response = {'result': result}
    return jsonify(result)


@schedule_blueprint.route('/create', methods=['POST'])
def create_schedule():
    try:
        schedule = Schedule()
        schedule.name = request.form['name']
        schedule.state = request.form['state']
        schedule.city = request.form['city']
        schedule.vaccination_cite = request.form['vaccination_cite']
        schedule.first_slot = request.form['first_slot']
        schedule.second_slot = request.form['second_slot']
        schedule.medical_condition = request.form['medical_condition']

        db.session.add(schedule)
        db.session.commit()

        response = {'message': 'Schedule created',
                    'result': schedule.serialize()}

    except Exception as e:
        print(str(e))
        response = {'message': 'Scheduled failed'}

    return jsonify(response)


@schedule_blueprint.route('/delete/<int:id>')
def delete(id):
    delete_schedule = Schedule.query.get_or_404(id)
    db.session.delete(delete_schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule deleted'})
