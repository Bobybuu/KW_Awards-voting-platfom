"""
Tests for the nominees endpoint
"""
import requests as req
import json

head = {"Content-Type": "application/json"}
link = "http://localhost:8000/api/"

endpoint = "nominees/"
with req.get(link + endpoint, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

# Create
nom = {"name": "Alpha",
       "description": "The first nominee",
       "category_ID": "Best Game Voice Actor"}
with req.post(link + endpoint, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

nom = {"name": "Beta",
       "description": "The second nominee",
       "category_ID": "18ec37fe-a3c9-4858-a732-49fb5d869aa2"}
with req.post(link + endpoint, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

nom = {"name": "Theta",
       "description": "The third nominee",
       "category_ID": "18ec37fe-a3c9-4858-a732-49fb5d869aa2"}
with req.post(link + endpoint, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

nom = {"name": "temp",
       "description": "The third nominee",
       "category_ID": "not There"}
with req.post(link + endpoint, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

# Get all
with req.get(link + endpoint, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(len(polo))
    print("")
    ID = polo[-1].get("ID")

# ID = "6232490e-7aac-4922-8112-e6b4eb0f5ba4" # Chosen from database
# with req.delete(link + "delete/" + ID, headers=head) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)

with req.get(link + endpoint + ID, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print(len(polo))
    print("")


edit = {"name": "Edited again"}
with req.put(link + endpoint + "put/" + ID, headers=head,
             data=json.dumps(edit)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

with req.get(link + endpoint + ID, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print("")
    print("")
    print(polo)
