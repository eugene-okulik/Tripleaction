import pytest
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.renew_post import RenewPost
from endpoints.delete_post import DeletePost
from endpoints.read_created_post import ReadPost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def read_created_post_endpoint():
    return ReadPost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def renew_post_endpoint():
    return RenewPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def post_id(create_post_endpoint):
    body = {"data": {"color": "verde", "size": "grande"}, "name": "Temp object"}
    response = create_post_endpoint.create_new_object(body)
    response_data = response.json()

    object_id = response_data.get("_id") or response_data.get("id")
    if not object_id:
        raise ValueError(f"Cannot get object ID from response: {response_data}")

    yield object_id
