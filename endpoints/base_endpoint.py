import allure


# import logging
#
# logging.getLogger(__name__)
# logging.basicConfig(level=logging.info())

class BaseEndpoint:
    response = None
    status_code = None
    response_json = None

    @allure.step('Check status code is 200')
    def check_status_code_is_200(self):
        assert self.status_code == 200

    @allure.step('Check status code is 404')
    def check_status_code_is_404(self):
        # logging.info(f'status code is {self.status_code}')
        assert self.status_code == 404

    @allure.step('Check that price is changed')
    def check_price_is_changed(self, price):
        assert self.response_json['data']['price'] == price
