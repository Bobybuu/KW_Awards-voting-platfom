"""
This file evaluates how the sub-categories associated endpoints work.
Should create the model first
"""
import requests as req
import json


link = "http://localhost:8000/api/"
head = {"Content-Type": "application/json"}

endpoint = "subcategories/"
# Create
# sub_cat = {
#     "name": "Best Film Actor",
#     "description": "Best actor in a film ",
#     "category_id": "447888ab-966a-48aa-9628-8fa8c73d775b"
# }
# with req.post(link + endpoint, headers=head,
#               data=json.dumps(sub_cat)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
#     print("")

# sub_cat2 = {
#     "name": "Best Series Actor",
#     "description": "Best actor in a series",
#     "category_id": "447888ab-966a-48aa-9628-8fa8c73d775b"
# }
# with req.post(link + endpoint, headers=head,
#               data=json.dumps(sub_cat2)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
#     print("")

# Get all
with req.get(link + endpoint, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")
    ID = polo[-1].get("id")

# Get the last object
with req.get(link + endpoint + ID, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

# Edit
# edit = {
#     "name": "Who is",
#     "description": "edited",
#     "category_id": "34034f0e-2caf-4e1c-abf7-f8aead4d9b01"
# }
# with req.put(link + endpoint + ID + "/", headers=head) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
#     print("")

# Delete
with req.delete(link + endpoint + ID + "/", headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")
