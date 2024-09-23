import json
import requests

url='https://cca9-35-238-213-152.ngrok-free.app/predict'

input_data_for_model={
    'N': 60,
    'P': 55,
    'K': 44,
    'temperature': 23.00445915,
    'humidity': 82.3207629,
    'ph': 7.840207144,
    'rainfall': 263.9642476
    }

input_json=json.dumps(input_data_for_model)
response=requests.post(url, data=input_json)

print(response.text)