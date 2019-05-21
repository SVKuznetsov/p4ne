import json
import requests
import pprint
import time




with open("C:\\PY_WORK\\card1.json") as f:
    cards = json.load(f)


for r in cards:
        num = str(r['CreditCard']['CardNumber'])[0:8]


        r = requests.get('https://lookup.binlist.net/'+num, headers={'Accept-Version': "3"})
        time.sleep(5)
        if 200 <= r.status_code <= 299:
            pprint.pprint(r.json())
        else:
            print(r.status_code)

