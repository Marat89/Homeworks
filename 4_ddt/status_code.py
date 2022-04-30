import pytest
import requests


def test_status_cod(base_url, status_code):
    r = requests.get(base_url)
    assert r.status_code == status_code
