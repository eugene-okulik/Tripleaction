import requests
import allure


class CreatePost:
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

    @allure.step("Check response code is 200")
    def check_status_code_is_correct(self, status_code):
        assert status_code == 200, "Status code is not 200"

    @allure.step("Check response color is the same as sent")
    def check_color_is_correct(self, expected_color):
        assert self.json["data"]["color"] == expected_color, "Color is not correct"

    @allure.step("Check response size is correct")
    def check_size_is_correct(self, expected_size):
        assert self.json["data"]["size"] == expected_size, "Size is not correct"

    @allure.step("Check response name is correct")
    def check_name_correct(self, expected_name):
        assert self.json["name"] == expected_name, "Name is not correct"
