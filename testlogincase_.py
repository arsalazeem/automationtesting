from selenium import webdriver
import xlrd
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

#adding dish
keyboard = Controller()
loc="C:\\Users\Arsal Azeem\\Desktop\\logindata.xlsx"
wb2 = openpyxl.open(loc)
sheet2 = wb2.active
wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
k=2

totalcount=sheet.nrows
for i in range(0,sheet.nrows-2):
    email=sheet.cell_value(k,0)
    p=sheet.cell_value(k,1)
    p=int(p)
    password=str(p)
    print(email)
    print(password)
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')

    try:
         driver.get("https://dev.tradishes.com/#/host/register")
         driver.implicitly_wait(40)
         driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/label').click()
         keyboard.press(Key.tab)
         keyboard.release(Key.tab)
         keyboard.type(email)
         keyboard.press(Key.tab)
         keyboard.release(Key.tab)
         keyboard.type(password)
         driver.find_element(By.XPATH, '//*[@id="submitLoginForm"]').click()
    except:
        print('nothing')

