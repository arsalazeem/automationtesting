from selenium import webdriver
import xlrd
import pdb
import openpyxl
from xlwt import Workbook
# import
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller
import initchrome

def start():
    opts = Options()
    opts.headless = True
    firefox_driver= webdriver.Firefox(options=opts, executable_path='C:\\Users\\ENSX-PC\\Desktop\\workspace\\Enabling\\firefox\\geckodriver.exe')
    return firefox_driver




