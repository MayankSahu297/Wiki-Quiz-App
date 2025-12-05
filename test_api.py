import requests
import json

url = "http://127.0.0.1:8000/generate"
payload = {"url": "https://en.wikipedia.org/wiki/Dog"}
headers = {"Content-Type": "application/json"}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=120)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 201:
        data = response.json()
        print("Success!")
        print(json.dumps(data, indent=2)[:500] + "...") # Print first 500 chars
    else:
        print("Error:", response.text)
except Exception as e:
    print("Exception:", e)
