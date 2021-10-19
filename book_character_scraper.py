from bs4 import BeautifulSoup
import requests
import json
import os

main_url = "https://harrypotter.fandom.com/wiki/"


def get_characters_by_book(book_url=None):

    r = requests.get(main_url + book_url)
    soup = BeautifulSoup(r.content, "lxml")

    character_dict = dict()
    context = soup.find("div", {"class": "mw-parser-output"})

    # Locate character by chapter
    tables = context.find_all("table")
    for i, chapter in enumerate(tables):
        list_of_characters = []
        characters = chapter.find_all("a")
        for character in characters:
            try:
                list_of_characters.append(
                    {"title": character["title"], "url": character["href"]}
                )
            except:
                pass

        character_dict["chapter_" + str(i + 1)] = list_of_characters

    return character_dict


def get_characters_by_book2(book_url=None, last_crop=0):

    if book_url == None:
        print(
            "Please provide the libk for the book from fandom. Ex: Harry_Potter_and_the_Philosopher%%27s_Stone_(character_index)"
        )

    r = requests.get(main_url + book_url)
    soup = BeautifulSoup(r.content, "lxml")

    character_dict = dict()
    context = soup.find("div", {"class": "mw-parser-output"})

    # Locate character by chapter

    uls = context.find_all(["ul", "dl", "p"])
    uls = uls[3 : len(uls) - last_crop]

    for i, characters_list in enumerate(uls):

        list_of_characters = []
        characters = characters_list.find_all("li")
        for character in characters:
            link = character.find("a")
            try:
                list_of_characters.append({"title": link["title"], "url": link["href"]})
            except:
                pass

        character_dict["chapter_" + str(i + 1)] = list_of_characters

    return character_dict


def get_characters_by_book3(book_url=None, last_crop=0):

    if book_url == None:
        print(
            "Please provide the libk for the book from fandom. Ex: Harry_Potter_and_the_Philosopher%%27s_Stone_(character_index)"
        )

    r = requests.get(main_url + book_url)
    soup = BeautifulSoup(r.content, "lxml")

    character_dict = dict()
    context = soup.find("div", {"class": "mw-parser-output"})

    # Locate character by chapter

    uls = context.find_all(["ul", "dl", "p"])
    uls = uls[3 : len(uls) - last_crop]

    for i, characters_list in enumerate(uls):

        list_of_characters = []
        characters = characters_list.find_all("li")
        for character in characters:
            link = character.find("a")
            try:
                list_of_characters.append({"title": link["title"], "url": link["href"]})
            except:
                pass

        character_dict["chapter_" + str(i + 1)] = list_of_characters

    return character_dict


books = [
    {
        "name": "philosophers_stone.json",
        "url": "Harry_Potter_and_the_Philosopher%27s_Stone_(character_index)",
    },
    {
        "name": "chamber_of_secrets.json",
        "url": "Harry_Potter_and_the_Chamber_of_Secrets_(character_index)",
    },
    {
        "name": "prisoner_of_azkaban.json",
        "url": "Harry_Potter_and_the_Prisoner_of_Azkaban_(character_index)",
    },
    {
        "name": "goblet_of_fire.json",
        "url": "Harry_Potter_and_the_Goblet_of_Fire_(character_index)",
    },
    {
        "name": "order_of_the_phoenix.json",
        "url": "Harry_Potter_and_the_Order_of_the_Phoenix_(character_index)",
    },
    {
        "name": "halfblood_prince.json",
        "url": "Harry_Potter_and_the_Half-Blood_Prince_(character_index)",
    },
    {
        "name": "deathly_hallows.json",
        "url": "Harry_Potter_and_the_Deathly_Hallows_(character_index)",
    },
]

crop_idxs = [0, 0, 1, 2, 1, 1, 1]

for idx, book in enumerate(books):
    if idx < 2:
        characters = get_characters_by_book(book_url=book["url"])
    elif idx == 5:
        characters = get_characters_by_book3(
            book_url=book["url"], last_crop=crop_idxs[idx]
        )
    else:
        characters = get_characters_by_book2(
            book_url=book["url"], last_crop=crop_idxs[idx]
        )

    with open(os.path.join("characters", book["name"]), "w") as f:
        json.dump(characters, f)
