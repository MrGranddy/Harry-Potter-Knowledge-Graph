from bs4 import BeautifulSoup
import requests
import json
import os

main_url = "https://harrypotter.fandom.com/"


def get_character_by_url(character_url):

    r = requests.get(main_url + character_url)
    soup = BeautifulSoup(r.content, "lxml")

    character_dict = dict()
    attributes = soup.find_all(
        "div", {"class": "pi-item pi-data pi-item-spacing pi-border-color"}
    )

    for attribute in attributes:
        key = attribute.find("h3", {"class": "pi-data-label pi-secondary-font"}).text
        value = attribute.find("div", {"class": "pi-data-value pi-font"})

        value_list = value.find("ul")
        if value_list is not None:
            items = []
            for value_item in value_list.find_all("li"):
                try:
                    link = value_item.find("a")
                    items.append( {"url": link["href"], "title": link["title"]} )
                except:
                    items.append( value_item.text )
                    
            value = items
        else:
            value = value.text

        character_dict[key] = value

    return character_dict

if __name__ == "__main__":

    with open("all_characters.json", "r") as f:
        characters_json = json.load(f)

    characters = []

    for idx, character in enumerate(characters_json):
        attributes = get_character_by_url(character["url"])
        characters.append( { **character, "attr": attributes } )

        if (idx + 1) % 100 == 0:
            print("%d / %d" % (idx+1, len(characters_json)))

    with open("attributes.json", "w") as f:
        json.dump(characters, f)
