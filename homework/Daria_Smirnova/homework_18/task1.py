import requests


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
    print(response.json())
    return response.json().get('id')


def one_object():
    object_id = new_object()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}')
    data = response.json()
    assert data['id'] == object_id
    print(data)


def post_object():
    body = {
        "data": {
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
    data = response.json()
    print(data)
    assert response.status_code == 201, 'Status code is incorrect'
    assert data['data']['color'] == 'verde', 'Color is incorrect'
    assert data['data']['size'] == 'grande', 'Size is incorrect'
    assert data['name'] == 'Primero object', 'Name is incorrect'
    clear(data['id'])


def put_object():
    object_id = new_object()
    body = {
        "data": {
            "color": "amarillo",
            "size": "medium"
        },
        "name": "Secundo object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    data = response.json()
    print(data)
    assert response.status_code == 200, 'Status code is incorrect'
    assert data['data']['color'] == 'amarillo', 'Color is incorrect'
    assert data['data']['size'] == 'medium', 'Size is incorrect'
    assert data['name'] == 'Secundo object', 'Name is incorrect'
    clear(object_id)


def patch_object():
    object_id = new_object()
    body = {
        "data": {
            "size": "pequeno"
        },
        "name": "Tercero object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    )
    data = response.json()
    print(data)
    assert response.status_code == 200, 'Status code is incorrect'
    assert data['data']['size'] == 'pequeno', 'Size is incorrect'
    assert data['name'] == 'Tercero object', 'Name is incorrect'
    clear(object_id)


def delete_object():
    object_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response.text)
    print(response.status_code)


def clear(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


post_object()
put_object()
patch_object()
delete_object()
