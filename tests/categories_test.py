"""
This file evaluates how the category associated endpoints work
"""
import requests as req
import json


link = "http://localhost:8000/api/"
head = {"Content-Type": "application/json"}

# Create a category
endpoint = "categories/"
category = {
    "name": "Films and Actors",
    "description": "Includes all related sub-categories"
}
# with req.post(link + endpoint, headers=head,
#               data=json.dumps(category)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
#     print("")

# category = {
#     "name": "Games",
#     "description": "Includes all related sub-categories"
# }
# with req.post(link + endpoint, headers=head,
#               data=json.dumps(category)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
#     print("")

# Pulls all categories
with req.get(link + endpoint, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    ID = polo[0].get("id")
    print("")

# Pulls a the first category
with req.get(link + endpoint + ID, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
