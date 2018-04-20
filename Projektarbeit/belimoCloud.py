#
# Device IDs
#    E-Valve 51: cd5c280f-5d59-4089-bd6a-e850e4cc400b
#    E-Valve 52: 1f6430af-9f00-4b55-bc8d-9ebbb10fad9e 
#    E-Valve 53: c2b4ec50-443a-49a4-8e77-0fd0a4268adf
#    E-Valve 54: 656cdd47-9950-4080-a416-f2a2b2202fb4
#
#
# Auth-Token (scheint immer gleich zu sein, sonst siehe OneNote Notebook): 
#    'Authorization':'Bearer 709628e9-c28a-4e48-b2ed-19289b202ad8'
#
#
#

import requests
import sys
import json
from pygments import highlight, lexers, formatters 


# Abfrage
resp = requests.get('https://cloud.belimo.com/api/v3/devices/cd5c280f-5d59-4089-bd6a-e850e4cc400b/data', headers={'Authorization':'Bearer 709628e9-c28a-4e48-b2ed-19289b202ad8'})

# HTTP-Status der Abfrage prüfen (200 = OK)
resp.status_code

# Inhalt anzeigen
resp.content
resp.json()



# Abfrage und Inhalt aufbereiten und anzeigen
resp = requests.get('https://cloud.belimo.com/api/v3/devices/cd5c280f-5d59-4089-bd6a-e850e4cc400b/data', headers={'Authorization':'Bearer 709628e9-c28a-4e48-b2ed-19289b202ad8'})
formatted_json = json.dumps(resp.json(), indent=4)
colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter()) 
print(colorful_json)



# Abfragen der letzten 10 Werte (limit=10) eines Datapoints (evcloud.150 = Temperature 1 embedded in Grad Kelvin) und anzeigen
resp = requests.get('https://cloud.belimo.com/api/v3/devices/cd5c280f-5d59-4089-bd6a-e850e4cc400b/data/history/datapoints/evcloud.150?limit=10', headers={'Authorization':'Bearer 709628e9-c28a-4e48-b2ed-19289b202ad8'})
resp.content

# Abfragen der letzten 10 Werte (limit=10) eines Datapoints (evcloud.150 = Temperature 1 embedded in Grad Kelvin) und formatiert anzeigen
resp = requests.get('https://cloud.belimo.com/api/v3/devices/cd5c280f-5d59-4089-bd6a-e850e4cc400b/data/history/datapoints/evcloud.150?limit=10', headers={'Authorization':'Bearer 709628e9-c28a-4e48-b2ed-19289b202ad8'})
formatted_json = json.dumps(resp.json(), indent=4)
colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter()) 
print(colorful_json)

