"""
This file evaluates how the awards associated endpoints work
"""
import requests as req
import json

head = {"Content-Type": "application/json"}
link = "http://localhost:8000/api/"

endpoint = "awards/"
award = {"name":"Best Game Voice Actor",
         "sub_category": "a12a16ea-b7d4-4bb2-895a-feffbc716b2a"}
# Create
with req.post(link + endpoint, headers=head,
              data=json.dumps(award)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

award2 = {"name": "Best Supporting Voice Actor",
          "sub_category": "a12a16ea-b7d4-4bb2-895a-feffbc716b2a"}
with req.post(link + endpoint, headers=head,
              data=json.dumps(award2)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

# Get all
with req.get(link + endpoint, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")
    ID = polo[-1].get("ID")

#  Get last one
with req.get(link + endpoint + ID, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

# Delete
# with req.delete(link + endpoint + "delete/" + ID, headers=head) as marko:
#     print(marko.status_code)

edit = {
    "name": "Who Is The Best Supporting Voice Actor",
}
with req.put(link + endpoint + "put/" + ID, headers=head,
             data=json.dumps(edit)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    print("")

# edit = {
#     "sub_category": "Actors"
# }
# with req.put(link + "put/" + ID, headers=head,
#              data=json.dumps(edit)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
