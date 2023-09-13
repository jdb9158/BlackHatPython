# Information Reconnaissance
# Grabs Banners, Hostname and IP Lookup

import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby + "\n")

#ipinfo.io

req2 = requests.get("https://ipinfo.io/" + gethostby + "/json")
response = json.loads(req2.text)

print("Location: " + response["loc"])
print("Region: " + response["region"])
print("City: " + response["city"])
print("Country: " + response["country"])
