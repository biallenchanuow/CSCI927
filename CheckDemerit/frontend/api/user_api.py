import requests
from flask import session, jsonify
from . import USER_API_URL, CHECKPOINTS_API_URL


class UserAPI:
    @staticmethod
    def login(data):
        url = USER_API_URL + '/api/user/login'
        response = requests.get(url=url, data=data)

        if response:
            return response.json()

    @staticmethod
    def get_user(email):
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
    def user_demerit_fetch(data):
        url = CHECKPOINTS_API_URL + '/api/checkpoints/user-fetch'
        response = requests.request("POST", url=url, data=data)
        if response:
            user = response.json()
            return user

    @staticmethod
    def edit_details(email, data):
        url = USER_API_URL + '/api/user/edit-details/' + email
        response = requests.request("POST", url=url, data=data)
        updated_information = {}
        if response:
            return response
        return updated_information



