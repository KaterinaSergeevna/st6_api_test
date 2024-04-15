import requests
import allure
from endpoints.base_endpoint import BaseEndpoint

import logging

logging.getLogger(__name__)
logging.basicConfig(level=logging.info('msg'))

HEADERS = {
    'Content-type': 'application/json'
}
PAYLOAD = {
    "name": "name",
    "data": {
        "year": 2022,
        "price": 2849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "12 TB"
    }
}


class CreatePublication(BaseEndpoint):

    @allure.step('Send post request')
    def create_new_publication(self, payload=None, headers=None):
        headers = headers if headers else HEADERS
        payload = payload if payload else PAYLOAD
        self.response = requests.post("https://api.restful-api.dev/objects", json=payload, headers=headers)
        self.status_code = self.response.status_code
        logging.info(f'status code is {self.status_code}')
        self.response_json = self.response.json()
        logging.info(f'status code is {self.response_json}')

    @allure.step('Check that title is correct')
    def check_title_is_(self, title):
        assert self.response_json['name'] == title
