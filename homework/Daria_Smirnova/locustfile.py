from locust import task, HttpUser, between
import random


class PostUser(HttpUser):
    wait_time = between(1, 3)

    def __init__(self, environment):
        super().__init__(environment)
        self.created_objects = []

    @task(4)
    def post_one_object(self):
        data = {
            "name": "Performance",
            "data": {"color": "rojo", "size": "grande"}
        }
        response = self.client.post("/object", json=data)
        if response.status_code == 201:
            object_id = response.json().get("id")
            if object_id:
                self.created_objects.append(object_id)

    def on_stop(self):
        for obj_id in self.created_objects:
            resp = self.client.delete(f"/object/{obj_id}")
            if resp.status_code not in [200, 204]:
                print(f"Failed to delete object {obj_id}: {resp.status_code}")

    @task(5)
    def get_one_object(self):
        self.client.get(
            f"/object/{random.choice([1917, 1918, 1919])}"
        )

    @task(3)
    def put_one_object(self):
        data = {
            "name": "Magnifico",
            "data": {"color": "blanco", "size": "changed"}
        }
        self.client.put(f"/object/1917", json=data)

    @task(2)
    def patch_one_object(self):
        data = {
            "name": "Incredible object"
        }
        self.client.patch(f"/object/1917", json=data)
