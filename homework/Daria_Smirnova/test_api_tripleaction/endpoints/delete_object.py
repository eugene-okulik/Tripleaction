import requests
import allure

from test_api_tripleaction.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    @allure.step("Delete object")
    def delete_object(self, object_id, headers=None):
        headers = headers or self.headers
        delete_url = f"{self.url}/{object_id}"
        self.response = requests.delete(delete_url, headers=headers)
        return self.response
