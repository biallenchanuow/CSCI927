import requests
from flask import session, jsonify
from frontend.api import USER_API_URL
from werkzeug.security import generate_password_hash, check_password_hash


class UserAPI:
    @staticmethod
    def login(email, password):
        data = {
            'email': email,
            'password': password
        }

        url = USER_API_URL + '/api/user/login'

        response = requests.post(url, data=data)
        if response:
            return jsonify(data.get('email'))

    @staticmethod
    def get_user(email):
        # headers = {
        #     'email': email
        # }
        url = USER_API_URL + f'/api/user/{email}'
        response = requests.get(url)
        return response.json

    @staticmethod
    def create_user(data):
        url = USER_API_URL + '/api/user/sign-up'
        response = requests.request("POST", url=url, data=data)
        if response:
            user = response.json()
            return user

    @staticmethod
    def edit_details(email, data):
        url = USER_API_URL + f'/api/user/edit-details/{email}'
        response = requests.post(url, data=data)
        if response:
            user = response.json()
            return user

