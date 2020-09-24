from selenium import webdriver
import xlrd

import pdb
import json

import openpyxl
from xlwt import Workbook
# import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller
import initchrome


def startorder(email,firstname,lastname,Adress1,Adress2,City,zipcode,phone_number,cardholdername,card_number,expiry_date,numberofkeys):
    try:
        buttonflag =4
        driver = initchrome.start()
        driver.get('https://dev.kardkey.com/#/')
        driver.implicitly_wait(40)
        driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/div[1]/div[1]/div/div[1]/button').click()
        buttonelement = driver.find_element(By.XPATH,
                                            '/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[3]/div/div/div/span[1]')

        # clicking button iteration
        for i in range(1, buttonflag):  # one quantity is already selected and loop runs number-1 times.
            buttonelement.click()
        # clicking button iteration ends.
        driver.find_element(By.XPATH,
                            '/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[4]/button[1]').click()
        driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(firstname)
        driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(lastname)
        driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys(Adress1)
        driver.find_element(By.XPATH, '//*[@id="address2"]').send_keys(Adress2)
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(City)
        # driver.find_element(By.XPATH,'//*[@id="country"]').click()
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("Pakistan")
        driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("Punjab")
        driver.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys("4600")
        driver.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys("03084512113")
        driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[4]/button').click()
        driver.find_element(By.XPATH, '//*[@id="shippingSelection"]').click()
        driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[4]/button').click()
        driver.find_element(By.XPATH, '//*[@id="cardholderName"]').send_keys("Arsal")
        driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys("4242424242424242424242424")
        driver.find_element(By.XPATH, '//*[@id="card_exp_input"]').send_keys("02/25")
        driver.find_element(By.XPATH, '//*[@id="card_exp_cvc"]').send_keys("356")
        driver.find_element(By.XPATH, '//*[@id="card_exp_zip"]').send_keys("4600")
        temp = driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[5]/div/button')
        time.sleep(5)
        temp.click()
        return driver
    except:
        return driver



