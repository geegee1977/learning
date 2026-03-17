import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "dnac_server.conf")


with open(filepath, "r") as f:
    data = f.read()

print(data)