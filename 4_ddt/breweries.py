import pytest
import requests
from jsonschema import validate


def test_list_breweries():
    r = requests.get("https://api.openbrewerydb.org/breweries")
    assert r.status_code == 200


@pytest.mark.parametrize("attribute, value", [
    ("state", "ohaio")
])
def test_breweries_by_attribute(attribute, value):
    r = requests.get(f"https://api.openbrewerydb.org/breweries?by_{attribute}={value}")
    for i in r.json():
        assert value in i[f'{attribute}']


""""Этот тест падает, из-за бага (а, возможно, и фичи) в апишке. Он проверяет, правильно ли была произведена выдача, 
ища совпадение с поисковым запросом в каждом 
значении ключа внутри итерации, если количество совпадений == 0, выдает ошибку (что он и делает). """


@pytest.mark.parametrize("query", ["dog", "beer", "ohio"])
def test_searh_breweries(query):
    r = requests.get("https://api.openbrewerydb.org/breweries/search?query=" + query)
    assert r.status_code == 200
    for i in r.json():
        math = 0
        for value in i.values():
            if value != None:
                if query.lower() in value.lower():
                    math += 1
            if value == None:
                continue
        assert math != 0


schema = {
    "id": "srt",
    "name": "str"
}
"""Этот тест падает так как превышено максимальное количество ответов выдачи """


@pytest.mark.parametrize('attribute_id', ['madtree-brewing-cincinnati', 'old-black-bear-brewing-madison'])
def test_get_brewery(attribute_id):
    r = requests.get(f"https://api.openbrewerydb.org/breweries/{attribute_id}")
    assert r.status_code == 200
    assert attribute_id == r.json()['id']
    assert len(r.json()) <= 15
    validate(instance=r.json(), schema=schema)
