import requests
import json
from serde_json import Value

# Define the data you want to send to the Rust API
data = {"key": "value"}

# Serialize the data to JSON format
serialized_data = json.dumps(data)

# Send the data to the Rust API
response = requests.post('http://localhost:8000/api', data=serialized_data)

# Check if the request was successful
if response.status_code == 200:
    # Deserialize the response from JSON format
    deserialized_response: Value = json.loads(response.text)
    print(deserialized_response)
else:
    print(f"Request failed with status code {response.status_code}")