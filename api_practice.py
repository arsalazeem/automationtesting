import requests
import json

currency=input()
url="https://free.currconv.com/api/v7/convert?q=USD_"+currency+"&compact=ultra&apiKey=80d83d62a167f6ce4e8e"
response=requests.get(url)
response=json.loads(response.content)
print(response)
temp="USD_IND"
temp2=response[temp]
print(temp2)