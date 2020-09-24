import requests
import json
import pdb
import logging
from datetime import date





def post_data(getalist):
    try:
        jsonlist = getalist
        payload = jsonlist
        url = 'https://portal.enabling.systems/api/testing'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(response.status_code)
        print(response.content)
    except Exception as e:
        print(e)






