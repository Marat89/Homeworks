import requests
import pytest
from jsonschema import validate
import json


@pytest.mark.parametrize('id', [1, 2, 3])
def test_status_get(id):
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    assert r.status_code == 200
    assert r.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert r.json()['id'] == id


headers = {"conten-type": "application/json; charset= UTF-8"}

data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1,
}

schema = {
    "title": 'str',
    "body": 'str',
    "userId": 'int',
}


def test_status_create_user():
    r = requests.post('https://jsonplaceholder.typicode.com/posts',
                      headers=headers,
                      json=data
                      )
    assert r.status_code == 201
    validate(instance=r.json(), schema=schema)


data2 = {
    "title": "qwe"
}


@pytest.mark.parametrize('id', [1, 2, 3])
def test_pathing(id):
    r = requests.put(f'https://jsonplaceholder.typicode.com/posts/{id}',
                     headers=headers,
                     json=data2
                     )
    assert r.status_code == 200
    assert r.json()["title"] == "qwe"


@pytest.mark.parametrize('id', [1, 2, 3])
def test_delete(id):
    r = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{id}')
    assert r.status_code == 200


def test_all_resources():
    r = requests.post('https://jsonplaceholder.typicode.com/posts')
    assert r.status_code == 201
    assert r.headers['Content-Type'] == 'application/json; charset=utf-8'
