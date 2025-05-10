import requests
import faker

base_url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev"

fake = faker.Faker()
for _ in range(5):
    response = requests.post(
        f"{base_url}/api/gigs",
        json={
            "venue_id": 0,
            "client_id": 1,
            "name": fake.text(),
            "date": fake.date(),
            "time": fake.time(pattern="%H:%M")
        },
    )
    print(f"Created Gig: {response.json()}")