import requests
import sys
import json
import time 


authToken = 'fe0cf642-5d57-4d89-95be-1825d98a04d4'

while True:
    with open('streamingDataSource.json', 'a') as outputfile:
        resp51 = requests.get('https://cloud.belimo.com/api/v3/devices/cd5c280f-5d59-4089-bd6a-e850e4cc400b/data', headers={'Authorization':'Bearer ' + authToken})
        outputfile.write(json.dumps(resp51.json())+ '\n')
        resp52 = requests.get('https://cloud.belimo.com/api/v3/devices/1f6430af-9f00-4b55-bc8d-9ebbb10fad9e/data', headers={'Authorization':'Bearer ' + authToken})
        outputfile.write(json.dumps(resp52.json())+ '\n')
        resp53 = requests.get('https://cloud.belimo.com/api/v3/devices/c2b4ec50-443a-49a4-8e77-0fd0a4268adf/data', headers={'Authorization':'Bearer ' + authToken})
        outputfile.write(json.dumps(resp53.json())+ '\n')
        resp54 = requests.get('https://cloud.belimo.com/api/v3/devices/656cdd47-9950-4080-a416-f2a2b2202fb4/data', headers={'Authorization':'Bearer ' + authToken})
        outputfile.write(json.dumps(resp54.json())+ '\n')
    time.sleep(20)

