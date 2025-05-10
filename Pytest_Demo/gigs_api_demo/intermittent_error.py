import requests


base_url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev"
data = {
  "email_address": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "phone_number": "string",
  "address": "string",
  "city": "string",
  "province": "string",
  "zip": "string",
  "country": "string"
}
token_data = {"username":"user1","password":"password"}
response = requests.post(f"{base_url}/token",data=token_data)
print(response)
token = response.json()["access_token"]

headers = {"Authorization":f"Bearer {token}"}
response = requests.post(f"{base_url}/api/clients",headers = headers, json = data)

for _ in range(10):
  response = requests.post(f"{base_url}/api/clients",headers = headers, json = data)
  client_id = response.json()['id']
  response = requests.get(f"{base_url}/api/clients/{client_id}",headers = headers, json = data)
  print(response.json())


