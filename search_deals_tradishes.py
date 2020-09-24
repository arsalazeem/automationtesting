from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 #searchdeal
print('Please input deal to search')
dealname=input()
driver=webdriver.Chrome(executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev.tradishes.com/#/customer/register")
element = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="submitLoginForm"]')))
print('ok')
driver.find_element(By.XPATH,'//*[@id="submitLoginForm"]').click()
time.sleep(15)
driver.find_element(By.XPATH,'//*[@id="search"]').send_keys(dealname)
driver.find_element(By.XPATH,'//*[@id="search-button"]/img').click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")



