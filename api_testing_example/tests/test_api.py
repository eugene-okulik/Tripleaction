import pytest

TEST_DATA = [
    {"text": "I always see advertisement everywhere", "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "tags": ["courses", "programming", "doctor"],
     "info": {"colors": ["blue", "brown"],
              "objects": ["picture", "text"]}
     },
]


@pytest.mark.parametrize("name", ["dasha_tester"])
def test_create_token(create_token_endpoint, name):
    body = {"name": name}
    create_token_endpoint.create_token("authorize", body)
    create_token_endpoint.check_status_code_is_200()



@pytest.mark.parametrize("data", TEST_DATA)
def test_create_one_meme(create_meme_endpoint, data):
    create_meme_endpoint.create_new_meme(body=data)
    create_meme_endpoint.check_status_code_is_200()
    create_meme_endpoint.check_text_is_correct(data["text"])
    create_meme_endpoint.check_url_is_correct(data["url"])
    create_meme_endpoint.check_tags_correct(data["tags"])
    create_meme_endpoint.check_info_colors_is_correct(data["info"], ["colors"])
    create_meme_endpoint.check_info_objects_is_correct(data["info"], ["objects"])
