import requests
import json

# API key from getorg.py
api_key = "bb37b6bf38563e79e0ecb30935cf28283e01f0fc"

# Organization ID for Decorus
org_id = "1713187"

# Meraki API endpoint for creating DNS local profile
url = f"https://api.meraki.com/api/v1/organizations/{org_id}/appliance/dns/local/records"

# Headers with API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Payload for the new DNS local profile
payload = {
    "hostname": "www.test.com",
    "address": "10.1.1.0",
    "profile": { "id": "4005951868546056228"}  # Replace with an actual profile ID from your organization
}

# Post the new DNS local profile
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    profile = response.json()
    print(f"Successfully created DNS local profile:")
    print(f"Response: {profile}")
    # print(f"ID: {profile['id']}")
    # print(f"Name: {profile['name']}")
else:
    print(f"Error: {response.status_code} - {response.text}")