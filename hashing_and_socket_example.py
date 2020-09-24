import initchrome
import requests
import json
import socket
import os
import hashlib

# encoding GeeksforGeeks using md5 hash
# function
result = hashlib.md5(b'GeeksforGeeks')

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.digest())





# a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# location = ("127.0.0.1", 80)
# result_of_check = a_socket.connect_ex(location)
#
# if result_of_check == 0:
#    print("Port is open")
# else:
#    print("Port is not open")

# response=requests.post("https://kardkey.com/",json="my name")
# print(response)

# a_socket.close()

# import login_instagram
# driver=login_instagram.login_insta()
# title=driver.title
# print(title)
# a=socket.gethostbyname(socket.gethostname())
#
# print(a)
# hostname = "https://gardne.com/"
# response = os.system("ping -c 1 " + hostname)
# try:
#     url = "https://gardne.com/"
#     for i in range(1, 20):
#         response = requests.get(url)
# except Exception as e:
#     print(e)


