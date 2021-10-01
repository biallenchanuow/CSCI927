import requests
from flask import session
from werkzeug.wrappers import response
from . import ADDRESS_API_URL


class AddressClient:
    @staticmethod
    def update(form):
        payload = {
            'email': form.email.data,
            'address1': form.address1.data,
            'address2': form.address2.data,
            'country': form.country.data,
            'state': form.state.data,
            'zipcode': form.zipcode.data
        }

        url = ADDRESS_API_URL + f'/api/address/update/{form.email.data}'

        response = requests.post(url, data=payload)

        if response:
            updated_information = response

        return updated_information.json()
