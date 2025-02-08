import requests as req
import json

data = {"name": "Alpha",
          "description": "first cat"}
head = {"Content-Type": "application/json"}
link = "http://localhost:8000/api/categories/"
with req.get(link) as marko:
    print(marko.status_code)
    print(marko.json())
