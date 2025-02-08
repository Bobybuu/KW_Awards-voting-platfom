import requests as req
import json

head = {"Content-Type": "application/json"}
link = "http://localhost:8000/api/awards/"

# award = {"name":"Best Programmer",
#          "sub_category": "Programmers"}
# with req.post(link, headers=head,
#               data=json.dumps(award)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)

# award2 = {"name": "Best Actor"}
# with req.post(link, headers=head,
#               data=json.dumps(award2)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)
#     ID = polo.get("ID")

# with req.get(link, headers=head) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)

# with req.get(link + ID, headers=head) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)

# ID = "291a37c2-7a06-4162-b865-ddb3298f2b5f"
# with req.delete(link + "delete/" + ID, headers=head) as marko:
#     print(marko.status_code)

ID = "9d9a3e89-71d0-4ccf-ae94-c41c36b13f36"
# edit = {
#     "name": "Who Is The Best Actor",
#     "sub_category": "Actors"
# }
# with req.put(link + "put/" + ID, headers=head,
#              data=json.dumps(edit)) as marko:
#     print(marko.status_code)
#     polo = marko.json()
#     print(polo)

edit = {
    "sub_category": "Actors"
}
with req.put(link + "put/" + ID, headers=head,
             data=json.dumps(edit)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
