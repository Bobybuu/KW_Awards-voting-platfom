"""
Tests for the nominees endpoint
"""
import requests as req
import json

head = {"Content-Type": "application/json"}
link = "http://localhost:8000/api/nominees/"

with req.get(link, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

nom = {"name": "Alpha",
       "description": "The first nominee",
       "category_ID": "Best Actor"}
with req.post(link, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

nom = {"name": "Beta",
       "description": "The second nominee",
       "category_ID": "Beta"}
with req.post(link, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

nom = {"name": "Theta",
       "description": "The third nominee",
       "category_ID": "7f7e9cbc-36ed-4151-aca8-130e0adb1300"}
with req.post(link, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

nom = {"name": "temp",
       "description": "The third nominee",
       "category_ID": "not There"}

with req.post(link, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

with req.get(link, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(len(polo))

# ID = "6232490e-7aac-4922-8112-e6b4eb0f5ba4" # Chosen from database
# with req.delete(link + "delete/" + ID, headers=head) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)

with req.get(link, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(len(polo))


ID = "d5cfc1bb-e497-49ad-9d4c-68c87817637b" # Chosen from database
edit = {"name": "Edited again"}
with req.put(link + "put/" + ID, headers=head,
             data=json.dumps(edit)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

ID = "d5cfc1bb-e497-49ad-9d4c-68c87817637b" # Chosen from database
with req.get(link + ID, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print("")
    print("")
    print(polo)
