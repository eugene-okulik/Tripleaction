import requests
import allure

from test_api_tripleaction.endpoints.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):

    @allure.step("Update previously created object")
    def update_object(self, object_id, body, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/{object_id}"
        self.response = requests.put(update_url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response
