#!/usr/bin/python3
import os, requests
from json import loads

VERSION_MANIFEST_URL="https://launchermeta.mojang.com/mc/game/version_manifest.json"
MINECRAFT_ROOT=os.environ["MINECRAFT_ROOT"]
TARGET_VERSION=os.environ["MINECRAFT_SERVER_VERSION"]

TARGET_DIR=MINECRAFT_ROOT + "/servers/" + TARGET_VERSION + "/"

if os.path.exists(TARGET_DIR + "server.jar"):
    print("File \"" + TARGET_DIR + "server.jar\" already exists, skipping...")
    exit(0)

raw_manifest = ""
try:
    print("Downloading \"" + VERSION_MANIFEST_URL + "\"...")
    raw_manifest = requests.get(VERSION_MANIFEST_URL).text
except Exception as e:
    print("Error: Cannot fetch \"" + VERSION_MANIFEST_URL + "\": {}".format(e))
    exit(1)
    pass

manifest = loads(raw_manifest)
found = False
url = ""
for version in manifest["versions"]:
    if TARGET_VERSION == version["id"]:
        found = True
        url = version["url"] 

if not found:
    print("Server version \"" + TARGET_VERSION + "\" not found!")
    exit(1)

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

try:
    server = requests.get(url)
    url = loads(server.text)["downloads"]["server"]["url"]

    print("Downloading \"" + url + "\"...")
    server = requests.get(url, allow_redirects=True)
    open(TARGET_DIR + "server.jar", "wb").write(server.content)
except Exception as e:
    print("Error: Cannot fetch \"" + url + "\": {}".format(e))
    exit(1)
    pass