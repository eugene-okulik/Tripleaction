import pytest

TEST_DATA = [
    {"data": {"color": "verde", "size": "grande"}, "name": "Primero object"},
    {"data": {"color": "rojo", "size": "pequeno"}, "name": "Secundo object"}
]


@pytest.mark.parametrize("data", TEST_DATA)
def test_create_one_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_status_code_is_200()
    create_object_endpoint.check_color_is_correct(data["data"]["color"])
    create_object_endpoint.check_size_is_correct(data["data"]["size"])
    create_object_endpoint.check_name_correct(data["name"])


def test_read_object(read_created_object_endpoint, post_id):
    read_created_object_endpoint.read_new_object(post_id)
    read_created_object_endpoint.check_status_code_is_200()


def test_put_object(update_object_endpoint, post_id):
    body = {
        "data": {"color": "amarillo", "size": "medium"},
        "name": "Updated object"
    }

    update_object_endpoint.update_object(object_id=post_id, body=body)
    update_object_endpoint.check_status_code_is_200()
    update_object_endpoint.check_color_is_correct(body["data"]["color"])
    update_object_endpoint.check_size_is_correct(body["data"]["size"])
    update_object_endpoint.check_name_correct(body["name"])


def test_patch_object(renew_object_endpoint, post_id):
    body = {
        "data": {
            "size": "muy pequeno"
        },
        "name": "Renewed_name object"
    }
    renew_object_endpoint.renew_object(object_id=post_id, body=body)
    renew_object_endpoint.check_status_code_is_200()
    renew_object_endpoint.check_size_is_correct(body["data"]["size"])
    renew_object_endpoint.check_name_correct(body["name"])


def test_delete_object(delete_object_endpoint, read_created_object_endpoint, post_id):
    delete_object_endpoint.delete_object(object_id=post_id)
    delete_object_endpoint.check_status_code_is_200()
    read_created_object_endpoint.check_object_not_exist(post_id)
