import requests
from werkzeug.wrappers import response
from flask import session
from . import Schedule_API_URL


class ScheduleClient:
    @staticmethod
    def get_schedules():
        header = {'Authorization': session['user_api_key']}
        response = requests.get(Schedule_API_URL +
                                '/api/schedule/all', headers=header)
        return response.json()

    @staticmethod
    def create_schedule(form):
        header = {'Authorization': session['user_api_key']}
        payload = {
            'name': form.name.data,
            'state': form.state.data,
            'city': form.city.data,
            'vaccination_cite': form.vaccination_cite.data,
            'first_slot': form.first_slot.data,
            'second_slot': form.second_slot.data,
            'medical_condition': form.medical_condition.data,
        }

        response = requests.post(Schedule_API_URL + '/api/schedule/create',
                                 data=payload, headers=header)
        return response.json()

    @staticmethod
    def get_schedule_from_session():
        default_schedule = {
            'items': {}
        }
        return session.get('schedule', default_schedule)
