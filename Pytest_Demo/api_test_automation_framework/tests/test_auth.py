import json

import requests

def test_create_token(session_token):

    url = "https://restful-booker.herokuapp.com/auth"
    token_value = session_token.get("token")

    payload = {json.dumps({"username": "admin", "password": "password123"})}
    headers = {
    'token': f'token={token_value}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200, 'Status code broken'
    assert response.url == url

