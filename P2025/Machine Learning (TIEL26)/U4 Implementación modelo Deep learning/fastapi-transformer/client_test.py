# client_test.py
import requests

url = "http://localhost:8000/predict"
data = {"text": "This movie was not absolutely amazing!"}
resp = requests.post(url, json=data)
print(resp.status_code, resp.json())
