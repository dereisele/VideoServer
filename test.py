import json
import xmltodict
from pprint import pprint

file = "contentdirectory"

with open(file + ".xml", "rb") as x:
    d = xmltodict.parse(x)

with open(file + ".json", "w") as j:
    json.dump(d, j, indent=4)
pprint(json)
