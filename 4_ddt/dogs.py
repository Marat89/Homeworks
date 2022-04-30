import pytest
import requests



@pytest.mark.parametrize("url, responce, sts",  [
    ("https://dog.ceo/api/breeds/list/all", 200, 'success'),
    ("https://dog.ceo/api/breeds/image/random", 200, 'success'),
    ("https://dog.ceo/api/breed/hound/images", 200, 'success'),
    ("https://dog.ceo/api/breed/hound/images", 200, 'success'),
    ("https://dog.ceo/api/breed/hound/list", 200, 'success'),
    ("https://dog.ceo/api/breed/eskimo/images/random", 200, 'success')

])
def test_request_status(url, responce, sts):
    r = requests.get(url)
    assert r.status_code == responce
    assert r.json()['status'] == sts