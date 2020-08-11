from selenium import webdriver
import xlrd
import xlsxwriter
import pdb
import json
import requests
import openpyxl
from xlwt import Workbook
# import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller

driver = webdriver.Chrome(
    executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.get('https://dev.kardkey.com/#/')
driver.implicitly_wait(40)
driver.find_element(By.XPATH,'/html/body/app-root/app-home/div/div[1]/div[1]/div/div[1]/button').click()
buttonelement=driver.find_element(By.XPATH,'/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[3]/div/div/div/span[1]')

#clicking button iteration
for i in range(1,buttonflag):    #one quantity is already selected and loop runs number-1 times.
    buttonelement.click()
#clicking button iteration ends.
driver.find_element(By.XPATH,'/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[4]/button[1]').click()
driver.find_element(By.XPATH,'//*[@id="Email"]').send_keys("azeemarsal@gmail.com")
driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("Arsal")
driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys("Azeem")
driver.find_element(By.XPATH,'//*[@id="address1"]').send_keys("E2 Olympia chemicals limited")
driver.find_element(By.XPATH,'//*[@id="address2"]').send_keys("E2 Olympica chemicals")
driver.find_element(By.XPATH,'//*[@id="city"]').send_keys("Islamabad")
# driver.find_element(By.XPATH,'//*[@id="country"]').click()
driver.find_element(By.XPATH,'//*[@id="country"]').send_keys("Pakistan")
driver.find_element(By.XPATH,'//*[@id="state"]').send_keys("Punjab")
driver.find_element(By.XPATH,'//*[@id="zipcode"]').send_keys("4600")
driver.find_element(By.XPATH,'//*[@id="phoneNumber"]').send_keys("03084512113")
driver.find_element(By.XPATH,'//*[@id="desktop"]/div[1]/div[4]/button').click()
driver.find_element(By.XPATH,'//*[@id="shippingSelection"]').click()
driver.find_element(By.XPATH,'//*[@id="desktop"]/div[1]/div[4]/button').click()
driver.find_element(By.XPATH,'//*[@id="cardholderName"]').send_keys("Arsal")
driver.find_element(By.XPATH,'//*[@id="cardNumber"]').send_keys("4242424242424242424242424")
driver.find_element(By.XPATH,'//*[@id="card_exp_input"]').send_keys("02/25")
driver.find_element(By.XPATH,'//*[@id="card_exp_cvc"]').send_keys("356")
driver.find_element(By.XPATH,'//*[@id="card_exp_zip"]').send_keys("4600")
pdb.set_trace()
temp=driver.find_element(By.XPATH,'//*[@id="desktop"]/div[1]/div[5]/div/button')
time.sleep(5)
temp.click()






# customlist = []
# for i in range(1,10):
#     a=str(i)
#     customdict="mydata" + "" + a
#     customdict = {}
#     customdict["name"] = "arsal azeem"
#     customdict["adress"]="Enabling Systems"
#     customlist.append(customdict)
#
#
#
# jsondata=json.dumps(customlist)
# response = requests.post('https://httpbin.org/post', jsondata)
# print("Status code: ", response.status_code)
# print("Printing Entire Post Request")
# print(response.json())
# print(jsondata)

