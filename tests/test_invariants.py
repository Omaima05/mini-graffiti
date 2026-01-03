import requests
import json

API_KEY = "AIzaSyBL3FMVdBhuLAk-EzK2XJ-oHfFrB6PLOj4"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(url)

print("Status:", response.status_code)
print(response.text)





