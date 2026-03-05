import json

# Open and load JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 90)
print(f"{'DN':50} {'Description':20} {'Speed':10} {'MTU':5}")
print("-" * 90)

# Navigate through JSON structure
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    
    print(f"{dn:50} {descr:20} {speed:10} {mtu:5}")