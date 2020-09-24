from datetime import date
import json


def toJson(a):
    return json.dumps(a, default=lambda o: o.__dict__)


def return_list_to_post(list_to_add,test,project,description,project_name):
    jsonlist = json.dumps(toJson(list_to_add))
    mainlist={}
    # this is the main list
    mainlist["Id"] = "0"
    mainlist["Test"] = test
    mainlist["Project"] = project
    mainlist["Description"] = description
    mainlist["MetaData"] = jsonlist
    mainlist["DateAdded"] = str(date.today())
    mainlist["DateUpdated"] = str(date.today())
    mainlist["ProjectName"] = project_name
    newdatalist = mainlist
    return newdatalist
