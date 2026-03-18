import requests
import os

# Get API key from user
# api_key = input("Enter your Meraki API key: ")
api_key = "ommited"

if not api_key:
    print("Error: MERAKI_API_KEY environment variable not set")
    exit(1)

# Meraki API endpoint
url = "https://api.meraki.com/api/v1/organizations"

# Headers with API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Get organizations
response = requests.get(url, headers=headers)

if response.status_code == 200:
    organizations = response.json()
    for org in organizations:
        print(f"ID: {org['id']}, Name: {org['name']}")
else:
    print(f"Error: {response.status_code} - {response.text}")

