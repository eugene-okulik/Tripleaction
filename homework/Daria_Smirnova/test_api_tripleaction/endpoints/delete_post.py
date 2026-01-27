import requests
import allure


class DeletePost:
    url = "http://167.172.172.115:52353/object/"
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

    @allure.step("Delete object")
    def delete_object(self, object_id, headers=None):
        headers = headers or self.headers
        delete_url = f"{self.url}/{object_id}"
        self.response = requests.delete(delete_url, headers=headers)
        return self.response

    @allure.step("Check response status code after object delete is 200")
    def check_status_code_is_correct(self, status_code):
        assert status_code == 200, f"Status code is not 200, got {status_code}"

    @allure.step("Check that object is deleted")
    def check_object_is_deleted(self, object_id):
        get_response = requests.get(f"{self.url}/{object_id}")
        assert get_response.status_code == 404, \
            'Object still exists after deletion'
