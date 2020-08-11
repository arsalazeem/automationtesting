from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://dev.tradishes.com/#/host/register")
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[6]/p/span').click()
time.sleep(50)
driver.find_element(By.XPATH,'//*[@id="submitRegistrationForm"]').click()
driver.find_element(By.XPATH,'//*[@id="kitchenForm01"]/div/div[1]/div/input').send_keys("03084512113")
time.sleep(50)
driver.find_element('//*[@id="kitchenForm01"]/div/div[3]/button').click()
time.sleep(60)
driver.find_element(By.XPATH,'//*[@id="kitchenForm"]/div[1]/input').send_keys("Arsal Azeem kitchen")
time.sleep(20)
driver.find_element(By.XPATH,'//*[@id="kitchenForm"]/div[1]/input').click()
time.sleep(15)
driver.find_element(By.XPATH,'//*[@id="kitchenForm11"]/div[4]/button').click()
time.sleep(15)
driver.find_element(By.XPATH,'//*[@id="kitchenForm3"]/div/div/button').click()
driver.find_element(By.XPATH,'//*[@id="kitchenForm4"]/div[2]/button').click()
