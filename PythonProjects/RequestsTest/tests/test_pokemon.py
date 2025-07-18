import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
Token = "user_token"
Header = {"Content-Type": "application/json", "trainer_token": Token}
trainer_id = '37814'

def test_status_code():
    response=requests.get(url=f'{URL}/trainers', headers=Header, params={'trainer_id': trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', headers=Header, params={'trainer_id': trainer_id})
    assert response_get.json()['data'][0]['trainer_name']== 'Викуля'