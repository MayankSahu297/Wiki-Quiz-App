import requests
import json

url = "http://127.0.0.1:8000/generate"
payload = {"url": "https://en.wikipedia.org/wiki/Cat"}
headers = {"Content-Type": "application/json"}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=120)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 201:
        data = response.json()
        
        # Save to file
        with open("api_response.json", "w") as f:
            json.dump(data, f, indent=2)
        
        print("\n=== API Response saved to api_response.json ===")
        print(f"Has 'quiz' key: {'quiz' in data}")
        if 'quiz' in data:
            print(f"Number of questions: {len(data['quiz'])}")
    else:
        print("Error:", response.text)
except Exception as e:
    print("Exception:", e)

