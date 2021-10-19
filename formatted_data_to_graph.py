import json

with open("formatted_data.json", "r") as f:
    formatted_data = json.load(f)

url_to_entity = {}
for character in formatted_data:
    url = character["url"]
    title = character["title"]
    attr = character["attr"]
    url_to_entity[url] = title

print(len(url_to_entity))

for character in formatted_data:
    url = character["url"]
    title = character["title"]
    attr = character["attr"]

    for key, value in attr.items():
        if type(value) == type([]):
            for item in value:
                if item["url"] not in url_to_entity:
                    url_to_entity[item["url"]] = item["title"]
                
print(len(url_to_entity))

source = []
target = []
relation = []

attributes = [ "Blood status", "Species", "House", "Nationality" ]
relations = [ "Family members", "Loyalty", "Occupation", "Romances" ]
relation_translate = ["is_family_member", "loyal_to", "occupies", "had_romance_with"]

for character in formatted_data:
    attr = character["attr"]
    s = url_to_entity[character["url"]]

    """
    if attr[ attributes[0] ] != None:
        source.append( s )
        target.append( attr[ attributes[0] ] )
        relation.append( "is" )

        source.append( attr[ attributes[0] ] )
        target.append( s )
        relation.append( "instance" )

    if attr[ attributes[1] ] != None:
        source.append( s )
        target.append( attributes[1]  )
        relation.append( "is" )
        
        source.append( attr[ attributes[1] ] )
        target.append( s )
        relation.append( "instance" )

    if attr[ attributes[2] ] != None:
        source.append( s )
        target.append( attributes[2]  )
        relation.append( "member_of" )
        
        source.append( attr[ attributes[2] ] )
        target.append( s )
        relation.append( "instance" )

    if attr[ attributes[3] ] != None:
        source.append( s )
        target.append( attributes[3]  )
        relation.append( "is" )
        
        source.append( attr[ attributes[3] ] )
        target.append( s )
        relation.append( "instance" )
    """

    for idx, r in enumerate(relations):

        if attr[ r ] != None:
            for item in attr[ r ]:
                source.append( s )
                target.append( url_to_entity[ item["url"] ] )
                relation.append( relation_translate[idx] )

with open("graph.json", "w") as f:

    json.dump({
        "source": source,
        "target": target,
        "relation": relation
    }, f)