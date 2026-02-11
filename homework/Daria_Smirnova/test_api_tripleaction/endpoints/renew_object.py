import requests
import allure

from test_api_tripleaction.endpoints.base_endpoint import BaseEndpoint


class RenewObject(BaseEndpoint):

    @allure.step("Renew new object")
    def renew_object(self, object_id, body, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/{object_id}"
        self.response = requests.patch(update_url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response
