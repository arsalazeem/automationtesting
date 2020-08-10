from selenium import webdriver
import xlrd
import xlsxwriter
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
keyboard=Controller()
# providing excel file location
loc="C:\\Users\Arsal Azeem\\Desktop\\testcases\\data.xlsx"
wb2 = openpyxl.open(loc)
sheet2 = wb2.active
print("Log")
wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
k=2
# reading excel rows count
for i in range(2,sheet.nrows):
    email=sheet.cell_value(i,0)  # reading row
    firstname=sheet.cell_value(i,1)
    lastname=sheet.cell_value(i,2)
    address1 = sheet.cell_value(i, 3)  # reading row
    address2 = sheet.cell_value(i, 4)
    city = sheet.cell_value(i, 5)
    zipcode= sheet.cell_value(i, 6)  # reading row
    phone_number= sheet.cell_value(i, 7)
    cardholdername = sheet.cell_value(i, 8)
    card_number = sheet.cell_value(i, 9)
    expiry_date = sheet.cell_value(i, 10)
    # print("email", email)
    # print("firstname", firstname)
    # print("lastname", lastname)
    # print("address1", address1)
    # print("address2", address2)
    # print("city", city)
    # print("zipcode", zipcode)
    # print("phone_number", phone_number)
    # print("CardHolderName", cardholdername)
    # print("Card Number", card_number)
    # print("Expiry date", expiry_date)
    # pdb.set_trace()
    # # iteration complete
    zipcode=int(zipcode)
    try:
        buttonflag = 4
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')
        driver.maximize_window()
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
        driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys(address1)
        driver.find_element(By.XPATH, '//*[@id="address2"]').send_keys(address2)
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(city)
        # driver.find_element(By.XPATH,'//*[@id="country"]').click()
        driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("pakistan")
        driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("Punjab")
        driver.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys(zipcode)
        driver.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys(str(int(phone_number)))
        driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[4]/button').click()
        driver.find_element(By.XPATH, '//*[@id="shippingSelection"]').click()
        driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[4]/button').click()
        driver.find_element(By.XPATH, '//*[@id="cardholderName"]').send_keys(cardholdername)
        driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys(card_number)
        driver.find_element(By.XPATH, '//*[@id="card_exp_input"]').send_keys(expiry_date)
        driver.find_element(By.XPATH, '//*[@id="card_exp_cvc"]').send_keys("356")
        driver.find_element(By.XPATH, '//*[@id="card_exp_zip"]').send_keys(zipcode)
        print("I am here at the final Button")
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[5]/div/button').click()
        print("Test case passed")
        k = i+1
        c1 = sheet2.cell(row=k, column=13)
        c1.value = "Pass"
        wb2.save(loc)
        print("Working till here")
        driver.quit()
    except:
        pdb.set_trace()
        print("Test case failed")
        k=i+1
        print("row index",i)
        c1 = sheet2.cell(row=k, column=13)
        c1.value = "failed"
        wb2.save(loc)
        driver.quit()






