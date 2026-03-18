import requests

# API key from getorg.py
api_key = "ommited"

# Organization ID for Decorus
org_id = "1713187"

# Meraki API endpoint for getting DNS local profiles
url = f"https://api.meraki.com/api/v1/organizations/{org_id}/appliance/dns/local/profiles"

# Headers with API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Get the DNS local profiles
response = requests.get(url, headers=headers)

if response.status_code == 200:
    profiles = response.json()
    print(f"Response: {profiles}")
    print(f"Type: {type(profiles)}")
    # print(f"Existing DNS local profiles in organization {org_id}:")
    for profile in profiles["items"]:
        print(f"ID: {profile['profileId']}, Name: {profile['name']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
