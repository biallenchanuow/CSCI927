import requests
from flask import session
from werkzeug.wrappers import response
from . import ADDRESS_API_URL


class AddressClient:
    @staticmethod
    def update(form):
        email = session['user']['email']
        payload = {
            'email': email,
            'address1': form.address1.data,
            'address2': form.address2.data,
            'country': form.country.data,
            'state': form.state.data,
            'zipcode': form.zipcode.data
        }

        url = ADDRESS_API_URL + f'/api/address/update/{email}'

        response = requests.post(url, data=payload)

        if response:
            updated_information = response

        return updated_information.json()


class UserClient:
    @staticmethod
    def login(form):
        api_key = None
        payload = {
            'email': form.email.data,
            'password': form.password.data
        }

        url = ADDRESS_API_URL + '/api/user/login'

        response = requests.post(url, data=payload)
        if response:
            api_key = response.json().get('api_key')
        return api_key

    @staticmethod
    def create_user(form):
        user = None
        payload = {
            'email': form.email.data,
            'password': form.password.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'gender': form.gender.data,
            'dob': form.dob.data,
            'licence_no': form.licence_no.data,
            'address1': form.address1.data,
            'address2': form.address2.data,
            'country': form.country.data,
            'state': form.state.data,
            'zipcode': form.zipcode.data
        }

        url = ADDRESS_API_URL + '/api/user/create'

        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def user_exists(email):
        url = ADDRESS_API_URL + 'api/user/' + email + '/exist'
        response = requests.get(url)
        return response.status_code == 200

    @staticmethod
    def get_user():
        headers = {
            'Authorization': session['user_api_key']
        }

        url = ADDRESS_API_URL + '/api/user/'
        response = requests.get(url, headers=headers)
        return response.json()
