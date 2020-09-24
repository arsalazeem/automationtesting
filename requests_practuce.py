from selenium import webdriver
import xlrd

import json
import xlsxwriter
import openpyxl
from xlwt import Workbook
# import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller
import requests
# driver = webdriver.Firefox(executable_path='C:\\Users\Arsal Azeem\\Desktop\\drivers\\geckodriver-v0.26.0-win64\\geckodriver.exe')
# driver.get("https://web.facebook.com")
# driver.implicitly_wait(40)
# driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("03023525115")
# driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys("(newpassword)123")
# driver.find_element(By.XPATH,'//*[@id="u_0_b"]').click()
# time.sleep(60)
# driver.get("https://web.facebook.com/ehsantariq23/")
# for i in range(1,30):
#     driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/divdri/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div').click()
#     driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys("Helo this is testing")
#     driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div').click()

result=requests.get('https://api.yelp.com/v3/businesses')
a=result.content
print(a)

# print(a)
# myname="aralazeem"
# data=json.dumps(myname)
# print(data)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# newlist=json.load(thisdict)
# print(type(newlist))
# print(rresult['origin'])
# rcontent=str(rcontent)
# rcontent=rcontent.replace("{",'')
# rcontent=rcontent.replace("}",'')
# rcontent=rcontent.replace(",",'')
# print(rcontent)
