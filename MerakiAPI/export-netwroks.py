import meraki
import pandas as pd

# ----------------------------------------------------------
# CONFIGURATION – fill these in
# ----------------------------------------------------------
API_KEY = "bb37b6bf38563e79e0ecb30935cf28283e01f0fc"
ORG_ID = "1010901"
NETWORK_ID = "L_3909687426511012314"
OUTPUT_FILE = "meraki_network_export.xlsx"
# ----------------------------------------------------------

dashboard = meraki.DashboardAPI(
    API_KEY,
    output_log=False,
    print_console=False
)

def safe_api_call(func, *args, **kwargs):
    """Wrapper to safely call the Meraki API and avoid crashes."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"API error in {func.__name__}: {e}")
        return None

# ----------------------------------------------------------
# COLLECT DATA
# ----------------------------------------------------------
data = {}

print("Fetching network details...")
data["Network"] = [safe_api_call(dashboard.networks.getNetwork, NETWORK_ID)]

print("Fetching devices...")
data["Devices"] = safe_api_call(dashboard.networks.getNetworkDevices, NETWORK_ID)

print("Fetching VLANs...")
data["VLANs"] = safe_api_call(dashboard.appliance.getNetworkApplianceVlans, NETWORK_ID)

print("Fetching SSIDs...")
data["SSIDs"] = safe_api_call(dashboard.wireless.getNetworkWirelessSsids, NETWORK_ID)

print("Fetching switch ports for all devices...")
switch_ports = []
devices = data["Devices"] or []
for d in devices:
    if "switch" in d.get("model", "").lower():
        ports = safe_api_call(dashboard.switch.getDeviceSwitchPorts, d["serial"])
        if ports:
            for p in ports:
                p["deviceSerial"] = d["serial"]
                switch_ports.append(p)
data["Switch Ports"] = switch_ports

print("Fetching firewall L3 rules...")
data["Firewall L3 Rules"] = [
    safe_api_call(dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules, NETWORK_ID)
]

print("Fetching firewall L7 rules...")
data["Firewall L7 Rules"] = safe_api_call(
    dashboard.appliance.getNetworkApplianceFirewallL7FirewallRules,
    NETWORK_ID
)

print("Fetching traffic shaping settings...")
data["Traffic Shaping"] = [
    safe_api_call(dashboard.appliance.getNetworkApplianceTrafficShaping, NETWORK_ID)
]

print("Fetching group policies...")
data["Group Policies"] = safe_api_call(
    dashboard.networks.getNetworkGroupPolicies, NETWORK_ID
)

print("Fetching organization admins...")
data["Admins"] = safe_api_call(
    dashboard.organizations.getOrganizationAdmins, ORG_ID
)

# ----------------------------------------------------------
# EXPORT TO EXCEL
# ----------------------------------------------------------
print(f"Writing data to {OUTPUT_FILE}...")

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    for sheet_name, content in data.items():
        if content is None:
            continue
        try:
            df = pd.DataFrame(content)
            df.to_excel(writer, index=False, sheet_name=sheet_name[:31])  # Excel max sheet name length
        except Exception as e:
            print(f"Error writing sheet {sheet_name}: {e}")

print("Export complete!")