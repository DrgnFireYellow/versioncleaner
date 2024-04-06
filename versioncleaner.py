import json
import shutil
import os

minecraftfolder = input("Enter the path to your .minecraft folder: ")

with open(os.path.join(minecraftfolder, "versions", "version_manifest_v2.json")) as versionmanifest:
    latestversion = json.load(versionmanifest)["latest"]

with open(os.path.join(minecraftfolder, "launcher_profiles.json")) as profilesfile:
    profiles = json.load(profilesfile)

usedversions = []

for profile in profiles["profiles"]:
    usedversions.append(profiles["profiles"][profile]["lastVersionId"])

for version in os.listdir(os.path.join(minecraftfolder, "versions")):
    if version not in usedversions and version != latestversion["release"] and version != latestversion["snapshot"] and os.path.isdir(os.path.join(minecraftfolder, "versions", version)):
        shutil.rmtree(os.path.join(minecraftfolder, "versions", version))
print("Done!")