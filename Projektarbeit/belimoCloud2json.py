#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import json
import time 

#
# Definition der Konstanten für
#    - Autorisierungs-Token
#    - Liste der 4 E-Valve 
#
authToken = 'Bearer fe0cf642-5d57-4d89-95be-1825d98a04d4'
eValves = ['https://cloud.belimo.com/api/v3/devices/cd5c280f-5d59-4089-bd6a-e850e4cc400b/data',
           'https://cloud.belimo.com/api/v3/devices/1f6430af-9f00-4b55-bc8d-9ebbb10fad9e/data',
           'https://cloud.belimo.com/api/v3/devices/c2b4ec50-443a-49a4-8e77-0fd0a4268adf/data',
           'https://cloud.belimo.com/api/v3/devices/656cdd47-9950-4080-a416-f2a2b2202fb4/data']

#
# Alle 20 Sekunden abholen der Daten pro E-Valve aus der BelimoCoreCloud
# und in das File auf dem Linux-File-System schreiben. Das File enthält 
# maximal einen Eintrag pro E-Valve und wird jedesmal überschrieben.
#
while True:
    with open('streamingDataSource.json', 'w') as outputfile:
        for eValve in eValves:
            response = requests.get(eValve, headers={'Authorization':authToken})
            outputfile.write(json.dumps(response.json())+ '\n')
    time.sleep(20)
