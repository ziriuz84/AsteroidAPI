import requests
import json

url = "http://127.0.0.1:8000/api/v1/target_list"

payload = json.dumps({
  "latitude": 9,
  "longitude": 44,
  "year": 2023,
  "month": 5,
  "day": 23,
  "hour": 21,
  "minute": 30,
  "max_objects": 50,
  "object_type": "cmt"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "http://127.0.0.1:8000/api/v1/neocp_confirmation"

payload = json.dumps({
  "latitude": 44,
  "longitude": 9,
  "min_score": 0,
  "max_magnitude": 30,
  "height": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

