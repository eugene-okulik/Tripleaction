import requests
import allure

from test_api_tripleaction.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    @allure.step("Create new object")
    def create_new_object(self, body, headers=None):
        headers = headers or self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response
