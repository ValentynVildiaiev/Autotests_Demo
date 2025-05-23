import os
import pytest
import requests
import json
import random
from ..src.services import CarApiService

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



@pytest.fixture(scope='session')
def sign_up_response(url):
    payload = json.dumps({
        "name": "John",
        "lastName": "Dou",
        "email": f"qweerty{random.randint(100000, 999999)}@mail.com",
        "password": "Test12341",
        "repeatPassword": "Test12341"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", f"{url}/auth/signup", headers=headers, data=payload, timeout=5)
    return response


@pytest.fixture(scope='session')
def headers(sign_up_response):
    return {'Cookie': f'sid={sign_up_response.cookies.get("sid")}'}


@pytest.fixture(scope='session')
def url():
    return os.environ['BASE_URL']


@pytest.fixture(scope='module')
def car_id(sign_up_response, headers):
    payload = json.dumps({
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1
    })
    response = CarApiService().create_new_car(body=payload, headers=headers)
    return response.get_field('data')['id']
