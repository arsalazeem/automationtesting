import initchrome
import datetime
import time
import requests
import pdb
from datetime import date
import json

def toJson(a):
    return json.dumps(a, default=lambda o: o.__dict__)



def checkk_loading_Time(project_name,description,url):
    driver = initchrome.start()
    time.sleep(7)
    intial_seconds = int(datetime.datetime.now().strftime("%S"))
    intial_minutes = int(datetime.datetime.now().strftime("%M"))
    driver.get(url)
    final_seconds = abs(int(datetime.datetime.now().strftime("%S")))
    final_minutes = int(datetime.datetime.now().strftime("%M"))
    total_time = str(final_minutes - intial_minutes) + " Minute" + " " + str(
        (final_seconds - intial_seconds)) + " " + "Seconds"
    print(total_time)
    response = requests.get(url)
    statuscode = str(response.status_code)
    if statuscode == "200":
        messege = "Site is Up"
        print(messege)
    print(statuscode)

    # this is the main list
    mainlist = {}
    jsonlist = []
    temp = {}
    temp["loading_time"] = total_time
    temp[project_name+"_site_status"] = messege
    jsonlist.append(temp)
    jsonlist = json.dumps(toJson(jsonlist))
    mainlist["Id"] = "0"
    mainlist["Test"] = "loading_time_and_website_Status"
    mainlist["Project"] = project_name
    mainlist["Description"] = description
    mainlist["MetaData"] = jsonlist
    mainlist["DateAdded"] = str(date.today())
    mainlist["DateUpdated"] = str(date.today())
    mainlist["ProjectName"] = project_name
    newdatalist = mainlist
    print(newdatalist)
    # return newdatalist
    # end of the main list



checkk_loading_Time("Gardne","To check loading time and site status","https://gardne.com/index.html")