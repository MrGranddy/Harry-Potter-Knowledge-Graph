import json
import os

with open("attributes.json", "r") as f:
    attributes = json.load(f)

attribute_set = set()

for character in attributes:
    title = character["title"]
    url = character["url"]
    attr = character["attr"]

    print(attr)

    attribute_set = attribute_set.union(attr.keys())

for attribute in sorted(list(attribute_set)):
    print(attribute)