import requests
from flask import session
from werkzeug.wrappers import response
from . import User_API_URL


class UserClient:
    @staticmethod
    def login(form):
        api_key = None
        payload = {
            'username': form.username.data,
            'password': form.password.data
        }

        url = User_API_URL + '/api/user/login'

        response = requests.post(url, data=payload)
        if response:
            api_key = response.json().get('api_key')
        return api_key

    @staticmethod
    def get_user():
        headers = {
            'Authorization': session['user_api_key']
        }

        url = User_API_URL + '/api/user/'
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def create_user(form):
        user = None
        payload = {
            'username': form.username.data,
            'password': form.password.data,
            'email': form.email.data,
            'phone': form.phone.data
        }

        url = User_API_URL + '/api/user/create'

        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def user_exists(username):
        url = User_API_URL + 'api/user/' + username + '/exists'
        response = requests.get(url)
        return response.status_code == 200

    @staticmethod
    def email_exists(email):
        url = User_API_URL + 'api/user/' + email + '/exist'
        response = requests.get(url)
        return response.status_code == 200

    @staticmethod
    def phone_exists(phone):
        url = User_API_URL + 'api/user/' + phone
        response = requests.get(url)
        return response.status_code == 200

    @staticmethod
    def user_admin():
        url = User_API_URL + 'admin/'
        response = requests.get(url)
        return response.json()
