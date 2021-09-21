import requests
from werkzeug.wrappers import response
from flask import session, request
#from . import Application_API_URL, User_API_URL

Application_API_URL = 'http://127.0.0.1:5002/'


class ApplicationClient:
    @staticmethod
    def get_applications():
        #header = {'Authorization': session['user_api_key']}
        response = requests.get(Application_API_URL +
                                '/api/application/all')  # headers=header)
        return response.json()

    @staticmethod
    def create_application(form):
        #header = {'Authorization': session['user_api_key']}
        payload = {
            'given_name': form.given_name.data,
            'family_name': form.family_name.data,
            'gender': form.gender.data,
            'indigenous_status': form.indigenous_status.data,
            'age': form.age.data,
            'place_of_birth': form.place_of_birth.data,
            'residential_address': form.residential_address.data,
            'residence_status': form.residence_status.data,
            'medicare': form.medicare.data,
            'vaccine_history': form.vaccine_history.data,
            'work_type': form.work_type.data,
            'booker_description': form.booker_description.data,
            'parking_required': form.parking_required.data,
            'interpreter_required': form.interpreter_required.data
        }

        response = requests.post(Application_API_URL + '/api/application/create',
                                 data=payload)  # headers=header)
        return response.json()

    @staticmethod
    def get_application_from_session():
        default_application = {
            'items': {}
        }
        return session.get('application', default_application)
