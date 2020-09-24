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


keyboard = Controller()

driver=webdriver.Chrome(executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev.tradishes.com/#/host/register")
driver.implicitly_wait(60)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[6]/p/span').click()
time.sleep(5)
keyboard.type("arsal")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("azeem")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("arsalazeem@ensx.com")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("12345678")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(60)
time.sleep(5)

