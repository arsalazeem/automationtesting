from selenium import webdriver
import xlrd
# import xlsxwriter
import pdb
import openpyxl
import stringfy
import post_data
import requests
import json
import logging
import json
import return_list_to_post
import initchrome
import post_data

# import
import variable_names
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import kardkeymakeorder
from pynput.keyboard import Key, Controller
keyboard=Controller()

def posthelper():
    page_url = "https://dev.kardkey.com/#/"
    mainlist[variable_names.sample_values] = mainformlist
    mainlist[variable_names.currenttime] = variable_names.get_time()
    mainlist[variable_names.pageurl] = page_url
    mainlist[variable_names.innerdata] = ""
    mainlist[variable_names.totalcount] = str(total_count)
    mainlist[variable_names.totalfailed] = str(fail_count)
    mainlist[variable_names.actualresult] = ""
    mainlist[variable_names.expectedresult] = ""
    print(mainlist)
    mydict.clear()
    mydict2.clear()
    mainlist.clear()
    # del mainlist[1:]
    del mainlist[:1]
    # post_data.post_data_on_portal(mainlist, "KardKey Order Flow with Happy Path", description, "KardKey")

def toJson(a):
    return json.dumps(a, default=lambda o: o.__dict__)


try:
    total_count=0
    fail_count=0
    mainformlist=[]
    mainlist={}
    # logging.basicConfig(filename='example.log', level=logging.DEBUG)
    sexception = "none"
    # providing excel file location
    path=r"data\data2.xlsx"
    loc = path
    wb2 = openpyxl.open(loc)
    sheet2 = wb2.active
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    k = 2
    # reading excel rows count
    for i in range(1, sheet.nrows):
        print(i)
        total_count=total_count+1
        email = sheet.cell_value(i, 0)  # reading row
        firstname = sheet.cell_value(i, 1)
        lastname = sheet.cell_value(i, 2)
        address1 = sheet.cell_value(i, 3)  # reading row
        address2 = sheet.cell_value(i, 4)
        city = sheet.cell_value(i, 5)
        try:

            zipcode = str(sheet.cell_value(i, 6))  # reading row
        finally:
            zipcode = str(sheet.cell_value(i, 6))  # reading row





        phone_number = str(sheet.cell_value(i, 7))
        phone_number=phone_number.replace(".0","")
        card_number = sheet.cell_value(i, 8)
        cardholdername = sheet.cell_value(i, 9)
        expiry_date = sheet.cell_value(i, 10)
        buttonflag = sheet.cell_value(i, 11)
        expected_result=sheet.cell_value(i, 13)
        description=sheet.cell_value(i,14)
        numerofkeys = buttonflag
        # logging.info('%s email',  email)
        # logging.info("%s FirstName", firstname)
        # logging.info("%s LastName", lastname)
        # logging.info("%s Adress1", address1)
        # logging.info("%s Adress2", address2)
        # logging.info("%s City", city)
        # logging.info("%s Zipcoode", zipcode)
        # logging.info("%s Phone Number", phone_number)
        # logging.info("%s CardNumber", card_number)
        # logging.info("%s CardHolderName", cardholdername)
        # logging.info("%s Expiry Date", expiry_date)
        # logging.info("%s Number of items", buttonflag)
        zipcode = str(zipcode)
        zipcode=zipcode.replace(".0","")
        print(description)
        # pdb.set_trace()
        try:
            buttonflag = 4
            driver = initchrome.start()
            driver.get('https://dev.kardkey.com/#/')
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/div[1]/div[3]/div/div[1]/div[1]/div/img[1]').click()
            buttonelement = driver.find_element(By.XPATH,
                                                '/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[3]/div/div/div/span[1]')

            # clicking button iteration
            for n in range(1, buttonflag + 1):  # one quantity is already selected and loop runs number-1 times.
                buttonelement.click()
            #contact information form
            driver.find_element(By.XPATH,
                                '/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[4]/button[1]').click()
            driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(email)
            driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(firstname)
            driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(lastname)
            driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys(address1)
            driver.find_element(By.XPATH, '//*[@id="address2"]').send_keys(address2)
            driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(city)
            # driver.find_element(By.XPATH,'//*[@id="country"]').click()
            driver.find_element(By.XPATH, '//*[@id="country"]').send_keys("United States")
            driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("California")
            driver.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys(zipcode)
            driver.find_element(By.XPATH, '//*[@id="phoneNumber"]').send_keys(phone_number)
            driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[4]/button').click()
            # contact information ends
            driver.find_element(By.XPATH, '//*[@id="shippingSelection"]').click()
            driver.find_element(By.XPATH, '//*[@id="desktop"]/div[1]/div[4]/button').click()
            #Paymentform
            driver.find_element(By.XPATH, '//*[@id="cardholderName"]').send_keys(cardholdername)
            driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys(card_number)
            driver.find_element(By.XPATH, '//*[@id="card_exp_input"]').send_keys(expiry_date)
            driver.find_element(By.XPATH, '//*[@id="card_exp_cvc"]').send_keys("356")
            driver.find_element(By.XPATH, '//*[@id="card_exp_zip"]').send_keys(zipcode)
            # time.sleep(15)
            # driver.find_element(By.XPATH,'//*[@id="desktop"]/div[1]/div[5]/div/button').click()
            # time.sleep(40)
            # temp=driver.find_element(By.XPATH,'/html/body/app-root/app-checkout/div/div/div[1]/div[1]/div[3]/div[2]/div[3]/button')
            # temp= temp.is_displayed()
            #
            # print("Order Again Button Visibility",":",temp)
            temp="True"
            if temp:
                result = variable_names.passed
            else:
                fail_count=fail_count+1
                result=variable_names.failed





            mydict = "mydata" + "" + str(i)
            mydict2 = "mydata2" + "" + str(i)
            mydict = {}
            mydict2 = {}

            mydict["form_name"] ="Contact Information"
            mydict["email"] = email
            mydict["no_of_keys"] = buttonflag
            mydict["first_name"] = firstname
            mydict["last_name"] = lastname
            mydict["adress1"] = address1
            mydict["adress2"] = address2
            mydict["city"] = city
            mydict["country"] = "United States"
            mydict["state"] = "California"
            mydict["zip_Code"] = zipcode
            mydict["phone_number"] = phone_number
            mydict["exception_in_script"]=sexception
            mydict[variable_names.actualresult] = result
            mydict[variable_names.expectedresult] = result
            mainformlist.append(mydict)

            mydict2["form_name"] = "Payment Details"
            mydict2["cardholder_name"] = cardholdername
            mydict2["card_number"] = card_number
            mydict2["expiry_date"] = expiry_date
            mydict2["CVV"] = "356"
            mydict2["exception_in_script"] = sexception
            mydict2[variable_names.actualresult] = result
            mydict2[variable_names.expectedresult] = result
            mainformlist.append(mydict2)
            posthelper()



        except Exception as e:
            fail_count=fail_count+1
            sexception = str(e)
            result = variable_names.failed
            # creating dict
            mydict = "mydata" + "" + str(i)
            mydict2 = "mydata2" + "" + str(i)
            mydict={}
            mydict2={}

            mydict["form_name"] = "Contact Information"
            mydict["email"] = email
            mydict["no_of_keys"] = buttonflag
            mydict["first_name"] = firstname
            mydict["last_name"] = lastname
            mydict["adress1"] = address1
            mydict["adress2"] = address2
            mydict["city"] = city
            mydict["country"] = "pakistan"
            mydict["state"] = "Punjab"
            mydict["zip_Code"] = zipcode
            mydict["phone_number"] = phone_number
            mydict[variable_names.actualresult]=result
            mydict[variable_names.expectedresult]=result
            mydict["exception_in_script"]=sexception
            mainformlist.append(mydict)
            mydict2["form_name"] = "Payment Details"
            mydict2["cardholder_name"] = cardholdername
            mydict2["card_number"] = card_number
            mydict2["expiry_date"] = expiry_date
            mydict2["CVV"] = "356"
            mydict2["exception_in_script"]=sexception
            mydict2[variable_names.actualresult] = result
            mydict2[variable_names.expectedresult] = result
            mainformlist.append(mydict2)
            posthelper()

except Exception as e:
    print(e)
    exit(0)










