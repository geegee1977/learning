
import requests
import time
import urllib3
from getpass import getpass
import os
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "dnac_server.conf")

with open(filepath, "r") as f:
 DNAC_IP = f.read()

DNAC_URL = "https://10.154.0.2"
USERNAME = input("Enter DNAC Username: ")
PASSWORD = getpass("Enter DNAC Password: ")

TOKEN = None
TOKEN_EXPIRES = 0

def get_token():
    global TOKEN, TOKEN_EXPIRES
    now = time.time()

    # Refresh token if missing or expired
    if TOKEN is None or now >= TOKEN_EXPIRES:
        url = f"{DNAC_URL}/dna/system/api/v1/auth/token"
        resp = requests.post(url, auth=(USERNAME, PASSWORD), verify=False)
        resp.raise_for_status()

        TOKEN = resp.json()["Token"]
        TOKEN_EXPIRES = now + 3600  # Token valid for 1 hour

    return TOKEN

def api_get(endpoint):
    token = get_token()
    headers = {"X-Auth-Token": token}
    url = f"{DNAC_URL}{endpoint}"

    resp = requests.get(url, headers=headers, verify=False)

    # If token expired early, refresh + retry once
    if resp.status_code == 401:
        TOKEN = None   # force refresh
        token = get_token()
        headers["X-Auth-Token"] = token
        resp = requests.get(url, headers=headers, verify=False)

    resp.raise_for_status()
    return resp.json()


# Test: Get network devices
devices = api_get("/dna/intent/api/v1/network-device?hostname=CWPMB0639")
#print(devices)

#print(TOKEN)
#print(TOKEN_EXPIRES)

#parsed = json.loads(devices)
print(json.dumps(devices, indent=4))