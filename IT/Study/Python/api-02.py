#!/usr/bin/python3

import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId":1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)

print("POSTing a new todo: " + str(response.json()))

if response.status_code == 201:
  print("POST successful!\n")
else:
  print("POST failed!\n")
