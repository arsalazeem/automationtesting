from selenium import webdriver
import xlrd
# import xlsxwriter
import pdb
import openpyxl
import json
import initchrome
from xlwt import Workbook
# import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import kardkeymakeorder
from pynput.keyboard import Key, Controller



driver=initchrome.start()
driver.get("https://dev.kardkey.com/#/")
script="alert('Test case passed');"
driver.execute_script(script)