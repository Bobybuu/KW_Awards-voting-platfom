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
       "category_ID": "76aea0b1-ff3d-44e3-97c0-ff973996c848"}
with req.post(link, headers=head, data=json.dumps(nom)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)
