import sendrequest
import json
from datetime import date
import pdb

def toJson(a):
    return json.dumps(a, default=lambda o: o.__dict__)


def post_data_on_portal(passlist, test_name, description, project_name,id):
    n_passlist=toJson(passlist)
    #
    mainlist={}
    mainlist["Id"] = "0"
    mainlist["Test"] = test_name
    # mainlist["Project"] = project_name
    mainlist["Description"] = description
    mainlist["MetaData"] = n_passlist
    mainlist["DateAdded"] = str(date.today())
    mainlist["DateUpdated"] = str(date.today())
    mainlist["ProjectName"] = project_name
    mainlist["ProjectId"]=id
    print(mainlist)
    pdb.set_trace()
    sendrequest.post_data(mainlist)
    #


