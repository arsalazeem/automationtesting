import requests
import json
import pdb

mylist=[]
print(type(mylist))
pdb.set_trace()
for i in range(1,10):
    templist="customlist"+str(i)
    templist=[]
    templist["name"]="arsalazeem"
    mylist.append(templist)
