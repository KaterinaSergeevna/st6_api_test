import requests
import allure
from endpoints.json_schemas import Publications
from endpoints.base_endpoint import BaseEndpoint

import logging

logging.getLogger(__name__)
logging.basicConfig(level=logging.info('msg'))


class GetPublication(BaseEndpoint):
    response_date = None

    @allure.step('send get request')
    def get_by_id(self, post_id):
        self.response = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
        self.status_code = self.response.status_code
        logging.info(f'status code is {self.status_code}')
        self.response_json = self.response.json()
        logging.info(f'status code is {self.response_json}')
        if self.status_code != 404:
            self.response_date = Publications(**self.response_json)

    @allure.step('Check id')
    def check_that_id_is(self, post_id):
        assert self.response_date.id == post_id
