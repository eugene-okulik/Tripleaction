import requests
import allure

from test_api_tripleaction.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step("Check that object is deleted")
    def check_object_is_deleted(self, object_id):
        get_response = requests.get(f"{self.url}/{object_id}")
        assert get_response.status_code == 404, \
            'Object still exists after deletion'
