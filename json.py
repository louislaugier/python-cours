import json

mon_json = """
"""

mon_json = """{"une_cle":23, "une_autre_cle":"test"}"""

json.loads(mon_json)

result = json.loads(mon_json)

type(result)

un_dict={
    1:2,
    2:3,
    4:5,
}

json.dumps(result)

json.load(json.dumps(result))

with open("./mon_json.json", "w") as mon_fichier:
    json.dump(result, mon_fichier, sort_keys=True, indent=4)

print(json.dumps(result, sort_keys=True, indent=4))

with open("./mon_json.json", "r") as mon_fichier:
    data = json.load(mon_fichier)

print(data)

print(result == data)
