import requests
import allure


class ReadPost:
    url = "http://167.172.172.115:52353/object"
    headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.response = None
        self.json = None

    @allure.step("Create new object")
    def create_new_object(self, body, headers=None):
        headers = headers or self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response

    @allure.step("Get information for new created object")
    def read_new_object(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        self.json = self.response.json()
        return self.response

    @allure.step("Check id is correct")
    def check_id_is_correct(self, expected_id):
        assert self.json['id'] == expected_id
