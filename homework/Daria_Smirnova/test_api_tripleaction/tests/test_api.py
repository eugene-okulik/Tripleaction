import pytest

TEST_DATA = [
    {"data": {"color": "verde", "size": "grande"}, "name": "Primero object"},
    {"data": {"color": "rojo", "size": "pequeno"}, "name": "Secundo object"}
]


@pytest.mark.parametrize("data", TEST_DATA)
def test_post_one_object(create_post_endpoint, data):
    response = create_post_endpoint.create_new_object(body=data)
    create_post_endpoint.check_status_code_is_correct(response.status_code)
    create_post_endpoint.check_color_is_correct(data["data"]["color"])
    create_post_endpoint.check_size_is_correct(data["data"]["size"])
    create_post_endpoint.check_name_correct(data["name"])


def test_read_object(read_created_post_endpoint, post_id):
    read_created_post_endpoint.check_id_is_correct(post_id)


def test_put_object(update_post_endpoint, post_id):
    body = {
        "data": {"color": "amarillo", "size": "medium"},
        "name": "Updated object"
    }

    response = update_post_endpoint.update_object(object_id=post_id, body=body)
    update_post_endpoint.check_status_code_is_correct(response.status_code)
    update_post_endpoint.check_color_is_correct(body["data"]["color"])
    update_post_endpoint.check_size_is_correct(body["data"]["size"])
    update_post_endpoint.check_name_correct(body["name"])


def test_patch_object(renew_post_endpoint, post_id):
    body = {
        "data": {
            "size": "muy pequeno"
        },
        "name": "Renewed_name object"
    }
    response = renew_post_endpoint.renew_object(object_id=post_id, body=body)
    renew_post_endpoint.check_status_code_is_correct(response.status_code)
    renew_post_endpoint.check_size_is_correct(body["data"]["size"])
    renew_post_endpoint.check_name_correct(body["name"])


def test_delete_object(delete_post_endpoint, post_id):
    response = delete_post_endpoint.delete_object(object_id=post_id)
    delete_post_endpoint.check_status_code_is_correct(response.status_code)
