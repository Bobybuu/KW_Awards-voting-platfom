"""
Tests for the category endpoint
"""
import requests as req
import json

head = {"Content-Type": "application/json"}

link = "http://localhost:8000/api/categories/"
with req.get(link, headers=head) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

cat = {"name": "Alpha",
       "description":"first cat"}
with req.post(link, headers=head, data=json.dumps(cat)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)

cat2 = {"name": "Beta",
        "description":"second cat"}
with req.post(link, headers=head, data=json.dumps(cat2)) as marko:
    print(marko.status_code)
    polo = marko.json()
    print(polo)