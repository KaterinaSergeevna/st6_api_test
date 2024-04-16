import allure
from tests.base_test import BaseTest


class TestApi(BaseTest):

    # @pytest.mark.parametrize('title', ['MY_Apple', '4'])
    def test_create_object (self):
        data = {
            "name": 'MY_Apple',
            "data": {
                "year": 2022,
                "price": 2849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "12 TB"
            }
        }
        self.create_ends.create_new_publication(payload=data)
        self.create_ends.check_status_code_is_200()
        self.create_ends.check_title_is_(data['name'])

    @allure.feature('Objects')
    @allure.story('Get object')
    def test_get_by_id(self, post_id):
        self.get_ends.get_by_id(post_id)
        self.get_ends.check_status_code_is_200()
        self.get_ends.check_that_id_is(post_id)

    def test_delete_pub(self, post_id):
        self.delete_ends.delete(post_id)
        self.delete_ends.check_status_code_is_200()
        self.get_ends.get_by_id(post_id)
        self.get_ends.check_status_code_is_404()

    def test_put_pub(self, post_id):
        put_payload = {
            "name": "MY_Apple MacBook Pro 16100",
            "data": {
                "year": 2014,
                "price": 4849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "120 TB"
            }
        }
        self.put_ends.send_put_request(post_id)
        self.put_ends.check_year_is_changed(put_payload['data']['year'])
        self.put_ends.check_price_is_changed(put_payload['data']['price'])
        self.put_ends.check_hard_disk_is_changed(put_payload['data']['Hard disk size'])

    def test_patch_pub(self, post_id):
        patch_payload = {
            "name": "MY_Apple MacBook Pro 1610",
            "data": {
                "price": 5849.99
            }
        }
        self.patch_ends.send_patch_request(post_id)
        self.patch_ends.check_price_is_changed(patch_payload['data']['price'])
        self.patch_ends.check_name_is_changed(patch_payload['name'])
