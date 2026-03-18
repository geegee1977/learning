import requests
import json

# API key from getorg.py
api_key = "ommited"

# Organization ID for Decorus
org_id = "1713187"

# Meraki API endpoint for creating DNS local profile
url = f"https://api.meraki.com/api/v1/organizations/{org_id}/appliance/dns/local/profiles"

# Headers with API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


# Post the new DNS local profile
response = requests.get(url, headers=headers)


if response.status_code == 200:
    dnsprofiles = response.json()
    for profile in dnsprofiles["items"]:
        print(f"DNS Profile ID: {profile['profileId']}, Name: {profile['name']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
