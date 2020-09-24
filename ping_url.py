import os
import subprocess
import requests

while 1==1:
    try:
        number="nothing"
        number=number+number
        response=requests.post("https://tradishes.com/", json=number)
        print(response.status_code)

    except Exception as e:
        print(e)

