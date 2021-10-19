import json
import re

with open("attributes.json", "r") as f:
    attributes = json.load(f)

with open("selected_categories.txt", "r") as f:
    categories = [line.strip() for line in f]

formatted_data = []

for character in attributes:
    selected_attributes = {}
    for category in categories:
        if category in character["attr"]:
            selected_attributes[category] = character["attr"][category]
        else:
            selected_attributes[category] = None
    formatted_data.append( {"url": character["url"], "title": character["title"], "attr": selected_attributes} )

_formatted_data = []

num_eliminate = 0
for character in formatted_data:
    none_count = 0
    for key, val in character["attr"].items():
        if val == None:
            none_count += 1
    if none_count >= 9:
        num_eliminate += 1
    else:
        _formatted_data.append( character )

print("%d / %d" % (len(_formatted_data), len(formatted_data)))
formatted_data = _formatted_data



category = categories[0]
#token_set = set()
for character in formatted_data:
    token = character["attr"][category]
    if token != None:
        token = re.sub("[\(\[].*?[\)\]]", "", token).strip().lower()

    if token == None:
        token = "unknown"
    elif "muggle-born" in token:
        token = "muggle-born"
    elif "muggle" in token:
        token = "muggle"
    elif "squib" in token:
        token = "squib"
    elif "half-blood" in token:
        token = "half-blood"
    elif "pure-blood" in token:
        token = "pure-blood"
    elif "veela" in token:
        token = "part-veela"
    elif " " in token:
        token = "unknown"

    character["attr"][category] = token
    
    #token_set.add(token)
#print(token_set)

category = categories[1]
for character in formatted_data:
    token = character["attr"][category]
    if token != None:
        years = re.findall("[0-9]{3,4}", token)
        if len(years) == 0:
            if "Middle Ages" in token:
                token = 1000
            else:
                years = re.findall("[0-9]{1,2}[a-z]{2} century", token)
                if len(years) != 0:
                    token = (int(re.findall("[0-9]{1,2}", years[0])[0]) - 1) * 100 + 50               
                else:
                    token = None
        else:
            token = int(years[0])

    character["attr"][category] = token

category = categories[2]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = "unknown"
    elif type(token[0]) == type({}):
        species = [x["title"] for x in token]
        if "Ghost" in species:
            token = "ghost"
        else:
            token = species[0].lower()
    else:
        token = re.sub("[\(\[].*?[\)\]]", "", token).strip().lower()
        if "veela" in token:
            token = "part-veela"
        elif "giant" in token:
            token = "giant"
        else:
            token = token.split()[-1]
    character["attr"][category] = token

category = categories[3]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = None
    elif type(token) == type([]):
        _tokens = []
        for t in token:
            if type({}) == type(t):
                _tokens.append(t)
        token = _tokens
    else:
        token = None

    character["attr"][category] = token

#house_set = set()
category = categories[4]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = "unknown"
    else:
        token = re.sub("[\(\[].*?[\)\]]", "", token).strip().lower()
        if " " in token:
            token = "unknown"
    #house_set.add(token)
    character["attr"][category] = token
#print(house_set)

category = categories[5]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = None
    elif type(token) == type([]):
        _tokens = []
        for t in token:
            if type({}) == type(t):
                _tokens.append(t)
        token = _tokens
    else:
        token = None

    character["attr"][category] = token

category = categories[6]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = "unknown"
    else:
        token = re.sub("[\(\[].*?[\)\]]", "", token).strip().lower()
        if "or" in token:
            token = [x.strip() for x in token.split()][0]
    
    character["attr"][category] = token

category = categories[7]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = None
    elif type(token) == type([]):
        _tokens = []
        for t in token:
            if type({}) == type(t):
                _tokens.append(t)
        token = _tokens
    else:
        token = None

    character["attr"][category] = token

category = categories[8]
for character in formatted_data:
    token = character["attr"][category]
    if token == None:
        token = None
    elif type(token) == type([]):
        _tokens = []
        for t in token:
            if type({}) == type(t):
                _tokens.append(t)
        token = _tokens
    else:
        token = None

    character["attr"][category] = token

with open("formatted_data.json", "w") as f:
    json.dump(formatted_data, f)