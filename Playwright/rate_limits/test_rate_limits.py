import requests

session = requests.session()
base_url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev"
data = {
  "date": "2025-05-07",
  "time": "23:51:41.907Z",
  "name": "ZimbaTest",
  "venue_id": 0,
  "client_id": 0
}

print("POST request limit check")
for _ in range(10):
    post_request = session.post(f"{base_url}/api/gigs",json=data)
    print(post_request.json())
    print("status:", post_request.status_code)
    gig_id = post_request.json()['id']
    post_request = session.delete(f"{base_url}/api/gigs/{gig_id}")
    print(f"Deleted gig:  {post_request.status_code}")
    if post_request.status_code == 429:
        print("Current limit reached: " )
        break


print("GET request limit check")
for _ in range(10):
    get_request = session.get(f"{base_url}/api/gigs")
    print(get_request.json())
    print("status:", get_request.status_code)
    if get_request.status_code == 429:
        print("Current limit reached: ")
        break

print("PUT request limit check")
for _ in range(100):
    put_request = session.put(f"{base_url}/api/gigs/108",json=data)
    print(put_request.json())
    print("status:", put_request.status_code)
    if put_request.status_code == 429:
        print("Current limit reached: ")
        break

print("DELETE request limit check")
for _ in range(100):
    post_request = session.post(f"{base_url}/api/gigs", json=data)
    print(post_request.json())
    print("status:", post_request.status_code)
    gig_id = post_request.json()['id']
    delete_request = session.delete(f"{base_url}/api/gigs/{gig_id}")
    print(f"Deleted gig:  {delete_request.status_code}")
    if delete_request.status_code == 429:
        print("Current limit reached: ")
        break









