import pytest
import requests


@pytest.fixture()
def new_object():
    body = {"data": {
        "color": "verde",
        "size": "grande"
    },
        "name": "Primero object"

    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json().get('id')
    print(object_id)
    yield object_id
    print('deleting the object')
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(scope='session', autouse=True)
def information():
    print('Start testing')
    yield
    print('End testing')


@pytest.fixture(autouse=True)
def before_and_after_each_test():
    print("before test")
    yield
    print("after test")


def test_get_one_object(new_object):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_object}')
    data = response.json()
    assert data['id'] == new_object
    print(data)


@pytest.mark.parametrize("color", ["rojo", "amarillo", "negro"])
@pytest.mark.critical
def test_post_one_object(color):
    body = {
        "data": {
            "color": color,
            "size": "grande"
        },
        "name": "Primero object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    data = response.json()
    print(data)
    assert response.status_code == 200, 'Status code is incorrect'
    assert data['data']['color'] == color, 'Color is incorrect'
    assert data['data']['size'] == 'grande', 'Size is incorrect'
    assert data['name'] == 'Primero object', 'Name is incorrect'


@pytest.mark.medium
def test_put_object(new_object):
    body = {
        "data": {
            "color": "amarillo",
            "size": "medium"
        },
        "name": "Secundo object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_object}',
        json=body,
        headers=headers
    )
    data = response.json()
    print(data)
    assert response.status_code == 200, 'Status code is incorrect'
    assert data['data']['color'] == 'amarillo', 'Color is incorrect'
    assert data['data']['size'] == 'medium', 'Size is incorrect'
    assert data['name'] == 'Secundo object', 'Name is incorrect'


def test_patch_object(new_object):
    body = {
        "data": {
            "size": "pequeno"
        },
        "name": "Tercero object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_object}',
        json=body,
        headers=headers
    )
    data = response.json()
    print(data)
    assert response.status_code == 200, 'Status code is incorrect'
    assert data['data']['size'] == 'pequeno', 'Size is incorrect'
    assert data['name'] == 'Tercero object', 'Name is incorrect'


def test_delete_object(new_object):
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_object}')
    assert response.status_code == 200, 'Status code is incorrect'
    get_response = requests.get(f'http://167.172.172.115:52353/object/{new_object}')
    assert get_response.status_code == 404, f'Object still exists after deletion'
