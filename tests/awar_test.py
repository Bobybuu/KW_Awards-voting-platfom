import requests as req
import json

head = {"Content-Type": "application/json"}
link = "http://localhost:8000/api/awards/"

award = {"name":"Best Programmer",
         "sub_category": "Programmers"}
with req.post(link, headers=head,
              data=json.dumps(award)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

award2 = {"name": "Best Actor"}
with req.post(link, headers=head,
              data=json.dumps(award2)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
    ID = polo.get("ID")

with req.get(link, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

# with req.get(link + ID, headers=head) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
