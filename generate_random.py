import random

num_list=[]
user_num=int(input())
def search(num):
    k=0
    for i in range(0,len(num_list)):
        if num_list[i]==num:
            k=k+1


    if k>0:
        return False
    else:
        return True

count=0
while(len(num_list)<9999):
    count=count+1
    temp_num=random.randint(0,9999)
    if search(temp_num):
        num_list.append(temp_num)
        #use the number as send key
        if temp_num==user_num:
            print("I found the user number at=",count)
            break
        else:
            print("working on found number=",count)
# import random
#
# count=0
# user_num=int(input())
# print("start")
# while 0==0:
#     count=count+1
#     temp_num=random.randint(0,999)
#     if temp_num==user_num:
#         print("I found the number on count:",count)
#         break




