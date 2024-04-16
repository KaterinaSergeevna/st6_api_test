import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step('Delete object')
    def delete(self, post_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
        self.status_code = self.response.status_code
