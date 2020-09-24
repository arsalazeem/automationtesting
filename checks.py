mydict={}
import variable_names
def createdict(*argv):
    mainlist=[]
    for arg in argv:
        myword=arg.split()
        mydict[myword[0]]=myword[1]
    mainlist.append(mydict)
    print(mainlist)


def make(a,b):
    a=str(a)
    b=str(b)
    return a+" "+b


createdict(make(variable_names.totalcount,5),make(variable_names.code,200))

#
#
# import requests
# a="nothing"
# for i in range(1,999):
#     a="This is nothing"+a
#
# print(a)
#
# print(requests.post("https://www.enabling.systems/", json=a).headers)
