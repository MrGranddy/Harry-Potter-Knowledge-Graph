import sys
import os
import json

if __name__ == "__main__":

    characters = []

    for file in os.listdir("characters"):
        path = os.path.join("characters", file)

        with open(path, "r") as f:
            character_dict = json.load(f)
            for chapter, character in character_dict.items():
                characters += character

    url_set = set()
    unique_characters = []

    for character in characters:
        if character["url"] not in url_set:
            unique_characters.append(character)
            url_set.add(character["url"])

    with open("all_characters.json", "w") as f:
        json.dump(unique_characters, f)
