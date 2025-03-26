import pytest
import requests
import json


@pytest.fixture(scope='session')
def session_token():
    url = "https://restful-booker.herokuapp.com/auth"

    payload = json.dumps({
        "username": "admin",
        "password": "password123"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_dict = json.loads(response.text)

    print(response.text)
    print(response.url)
    return response_dict
