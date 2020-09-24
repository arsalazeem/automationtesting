import time
from datetime import datetime
import requests
import json



def get_time():
    c_time=str(datetime.now())
    print(c_time)
    n_time=c_time[22:len(c_time)]
    c_time=c_time.replace(n_time,"")
    return c_time


pageurl="page_url"  #page url under testing
url="url" #indiviuals urls for inner page data
sample_values="sample_values"  #sample values used
innerdata="inner_data"  #inner page urls images or other tag links data
actualresult="actual_result"
expectedresult="expected_result"
status="status"  #indiviuals url status where inner data will be applicable
code="code"        #response code for invdivual urls in inner data object
currenttime="current_time"
passed="passed"
failed="failed"
totalcount="total_count"     #refers to total urls/images scanned
totalfailed="total_failed"   #refers to total failed images urls
statuscodepassed="pass"
statuscodefailed="error"
formname="form_name"
n_exception="exception_in_script"


def get_project_name(t_id)->int:
    try:
        response = requests.get("https://portal.enabling.systems/api/app/get-projects")
        response = json.loads(response.content)
        for a in response["data"]:
            if a["id"] == t_id:
                return a["id"], a["projectName"]
    except Exception as e:
        print(e)
        return a["NULL","NULL"]



def show_project_name():
    try:
        response = requests.get("https://portal.enabling.systems/api/app/get-projects")
        response = json.loads(response.content)
        for a in response["data"]:
            print(a)
        print("Please Select Project Id")
        num=input()
        project_info=get_project_name(int(num))
        print(project_info)
        return project_info
    except:
        print("There was a problem in fetching in project names please check your script")








#creating sample values
#1)Create new object on each iteration.
#2)Now append each of these objects in main array list.
#3)Each object should have same exact generic keys.


