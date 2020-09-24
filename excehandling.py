from selenium import webdriver
import pynput
import xlrd
import xlsxwriter
import openpyxl
from xlwt import Workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller


keyboard = Controller()
driver = webdriver.Chrome(
    executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev.tradishes.com/#/host/register")
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/label').click()
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("arsalazeem101@gmail.com")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("12345678")
driver.find_element(By.XPATH, '//*[@id="submitLoginForm"]').click()

# import xlsxwriter
# import openpyxl
# loc="C:\\Users\Arsal Azeem\\Desktop\\data.xlsx"
# wb = openpyxl.open(loc)
# sheet = wb.active
# c1 = sheet.cell(row = 3, column = 10)
# c1.value="arsal"
# wb.save(loc)
# wb=xlrd.open_workbook(loc)
# k=2
# sheet = wb.sheet_by_index(0)
#
# totalcount=sheet.nrows
# print(totalcount)
# for i in range(0,sheet.nrows-2):
#     print(sheet.cell_value(k, 2))
#     print(sheet.cell_value(k, 3))
#     print(sheet.cell_value(k, 4))
#     print(sheet.cell_value(k, 5))
#     k=k+1
#     print("next iteration")
