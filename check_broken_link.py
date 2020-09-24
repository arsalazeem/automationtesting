import requests
import json


response=requests.get("https://portal.enabling.systems/api/testing")
print(response.status_code)