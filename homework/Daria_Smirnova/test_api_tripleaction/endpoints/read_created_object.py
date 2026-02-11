import requests
import allure

from test_api_tripleaction.endpoints.base_endpoint import BaseEndpoint


class ReadObject(BaseEndpoint):

    @allure.step("Get information for new created object")
    def read_new_object(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        self.json = self.response.json()
        return self.response

    @allure.step("Check that object is not exist anymore")
    def check_object_not_exist(self, object_id):
        get_response = requests.get(f"{self.url}/{object_id}")
        assert get_response.status_code == 404, \
            'Object still exists after deletion'
