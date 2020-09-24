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

driver=webdriver.Chrome(executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev.tradishes.com/#/host/register")
driver.implicitly_wait(40)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/label').click()
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("arsalazeem101@gmail.com")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("12345678")
driver.find_element(By.XPATH, '//*[@id="submitLoginForm"]').click()
driver.find_element(By.XPATH,'//*[@id="customer-dining-container"]/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/img').click()
