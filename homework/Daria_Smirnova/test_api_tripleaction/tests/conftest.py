import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.renew_object import RenewObject
from endpoints.delete_object import DeleteObject
from endpoints.read_created_object import ReadObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def read_created_object_endpoint():
    return ReadObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def renew_object_endpoint():
    return RenewObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def post_id(create_object_endpoint):
    body = {"data": {"color": "verde", "size": "grande"}, "name": "Temp object"}
    response = create_object_endpoint.create_new_object(body)
    response_data = response.json()

    object_id = response_data.get("_id") or response_data.get("id")
    if not object_id:
        raise ValueError(f"Cannot get object ID from response: {response_data}")

    yield object_id
# test
