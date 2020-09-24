import initchrome
from selenium import webdriver
import xlrd
import pdb
import openpyxl
from xlwt import Workbook
# import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains

def openurl():
    driver = initchrome.start()
    driver.get("http://automationpractice.com/index.php")
    driver.implicitly_wait(60)
    time.sleep(30)
    action = ActionChains(driver)
    parent_level_menu = driver.find_element(By.XPATH,'//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img')
    action.move_to_element(parent_level_menu).perform()
    driver.find_element(By.XPATH,'//*[@id="homefeatured"]/li[4]/div/div[2]/div[2]/a[1]/span').click()
    time.sleep(60)

openurl()