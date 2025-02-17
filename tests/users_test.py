"""
This file evaluates how the user associated endpoints work
"""
import requests as req
import json


link = "http://localhost:8000/api/"
head = {"Content-Type": "application/json"}

# Create user
endpoint = "auth/signup"
user = {
    "first_name": "Megs",
    "last_name": "Chie",
    "email": "firstemail@test.com",
    "phone_number": "0123456789",
    "password": "password",
    "is_staff": True,
    "bio": "Beta tester"
}
with req.post(link + endpoint, headers=head,
              data=json.dumps(user)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

# To be completed
