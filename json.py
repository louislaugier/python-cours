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