import requests
import allure

class UpdatePost():
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

    @allure.step("Update previously created object")
    def update_object(self, object_id, body, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/{object_id}"
        self.response = requests.put(update_url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response

    @allure.step("Check response status code after object update is 200")
    def check_status_code_is_correct(self, status_code):
        assert status_code == 200, f"Status code is not 200, got {status_code}"

    @allure.step("Check response color is the same as sent")
    def check_color_is_correct(self, expected_color):
        assert self.json["data"]["color"] == expected_color, f"Color is not correct, got {self.json['data']['color']}"

    @allure.step("Check response size is the same as sent")
    def check_size_is_correct(self, expected_size):
        assert self.json["data"]["size"] == expected_size, f"Size is not correct, got {self.json['data']['size']}"

    @allure.step("Check response name is correct")
    def check_name_correct(self, expected_name):
        assert self.json["name"] == expected_name, f"Name is not correct, got {self.json['name']}"
