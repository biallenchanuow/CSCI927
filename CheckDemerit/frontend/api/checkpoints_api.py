import requests
from flask import session, jsonify
from frontend.api import CHECKPOINTS_API_URL
from werkzeug.security import generate_password_hash, check_password_hash


class CheckPointsAPI:
    @staticmethod
    def input_licence():
        pass

    @staticmethod
    def show_demerit(licence_no):
        url = CHECKPOINTS_API_URL + f'/api/checkpoints'
        response = requests.get(url, headers={"licence_no": licence_no})
        return response.json()