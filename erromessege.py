import requests
import json
import pdb

def return_error_messege():
    messege="unable to locate element"
    temp="this is sfsdf  unable to locate element sdfsd whgat else ou wnag <?pofsdfik"
    result_messege=temp.find(messege)
    index=-1
    if result_messege!=-1:
        return "Bad Internet Connection"


url="https://official-joke-api.appspot.com/random_joke"
for i in range(0,10):
    k = i
    print("Joke Number=" + str(k + 1))
    response_list = requests.get(url).content
    response_list = json.loads(response_list)
    print(response_list["setup"])
    print(response_list["punchline"])


