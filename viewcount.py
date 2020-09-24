from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev.tradishes.com/#/host/register")
time.sleep(60)
print('ok')
driver.find_element(By.XPATH,'//*[@id="submitLoginForm"]').click()
time.sleep(15)