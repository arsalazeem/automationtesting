import requests
import json

mylist = []



for i in range(1,5):
      a=str(i)
      dictname="mydata"+""+a
      dictname
      dictname={}
      dictname["name"] = "arsal"
      dictname["password"]="azeem"
      mylist.append(dictname)

mydata=json.dumps(mylist)
url='http://https://httpbin.org/post'
result=requests.post(url,data=str(mydata))
print(result.text)
# for i in range(1,5):
#     a = str(i)
#     dictname = "mydata" + "" + a



# for i in range(1,5):
#     a = str(i)
#     dictname2 = "mydata" + "" + a
#     mydata[dictname2]=dictname2


# print(mydata)

# released = {
# 		"iphone" : 2007,
# 		"iphone 3G" : 2008,
# 		"iphone 3GS" : 2009,
# 		"iphone 4" : 2010,
# 		"iphone 4S" : 2011,
# 		"iphone 5" : 2012
# 	}
#
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# #
# print(myfamily)