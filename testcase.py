from selenium import webdriver
import xlrd
import xlsxwriter
import openpyxl
import json
import pdb
from xlwt import Workbook
# import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller

#adding dish
add_dish_result=[]
# pdb.set_trace()
keyboard = Controller()
loc="C:\\Users\Arsal Azeem\\Desktop\\data.xlsx"
wb2 = openpyxl.open(loc)
sheet2 = wb2.active
wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
k=2

totalcount=sheet.nrows
for i in range(0,sheet.nrows-2):
    email=sheet.cell_value(k,0)
    p=sheet.cell_value(k,1)
    p=int(p)
    password=str(p)
    print(email)
    print(password)
    dishname = sheet.cell_value(k, 2)
    price = sheet.cell_value(k, 3)
    description = sheet.cell_value(k, 4)
    pickup_option = sheet.cell_value(k, 5)
    s_time=sheet.cell_value(k, 6)
    star_time=s_time
    e_time=str(sheet.cell_value(k, 7))
    end_time=e_time
    s_time_check=s_time[-2]
    e_time_check=e_time[-2]
    s_time=s_time[0] + "" + s_time[1]
    e_time = e_time[0] + "" + e_time[1]
    print(s_time,e_time)
    avialbility = str(sheet.cell_value(k, 8))
    print(dishname,price,description,pickup_option,s_time,e_time,avialbility)
    # pdb.set_trace()
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\Arsal Azeem\\Desktop\\drivers\\chromedriver_win32\\chromedriver.exe')

    try:
         driver.get("https://dev.tradishes.com/#/host/register")
         driver.implicitly_wait(40)
         driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/label').click()
         keyboard.press(Key.tab)
         keyboard.release(Key.tab)
         keyboard.type(email)
         keyboard.press(Key.tab)
         keyboard.release(Key.tab)
         keyboard.type(password)
         driver.find_element(By.XPATH, '//*[@id="submitLoginForm"]').click()
         driver.find_element(By.XPATH,
                             '//*[@id="customer-dining-container"]/div/div/div[2]/div/div[1]/div/div/button').click()
         # time.sleep(30)
         print(dishname)
         driver.find_element(By.XPATH, '//*[@id="title"]').send_keys(dishname)
         print(price)
         driver.find_element(By.XPATH, '//*[@id="price"]').send_keys(str(price))
         driver.find_element(By.XPATH, '//*[@id="description"]').send_keys(description)
         #driver.find_element(By.XPATH,'//*[@id="offer-image"]').send_keys("C:\\Users\Arsal Azeem\Desktop\\testpic.jpg")
         # //*[@id="addOffer2"]/div[1]/div/div[1]/div[2]/div[1]/div/input
         if pickup_option=="pickup":
             if s_time_check == "p":
                 driver.find_element(By.XPATH, '//*[@id="basic-addon1"]').click()
                 driver.find_element(By.XPATH, '//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-timer/div').click()
                 driver.find_element(By.XPATH,
                                     '//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-timer/owl-date-time-timer-box[1]/label/input').click()
                 keyboard.press(Key.right)
                 keyboard.release(Key.right)
                 keyboard.press(Key.right)
                 keyboard.release(Key.right)
                 keyboard.press(Key.backspace)
                 keyboard.release(Key.backspace)
                 keyboard.press(Key.backspace)
                 keyboard.release(Key.backspace)
                 driver.find_element(By.XPATH,'//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-timer/owl-date-time-timer-box[1]/label/input').send_keys(str(s_time))
                 time.sleep(10)
                 driver.find_element(By.XPATH, '//*[@id="owl-dt-picker-0"]/div[2]/div/button[2]/span').click()

             elif s_time_check == "a":
                 driver.find_element(By.XPATH, '//*[@id="basic-addon1"]').click()
                 # driver.find_element(By.XPATH, '//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-timer/div').click()
                 driver.find_element(By.XPATH,
                                     '//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-timer/owl-date-time-timer-box[1]/label/input').click()
                 keyboard.press(Key.right)
                 keyboard.release(Key.right)
                 keyboard.press(Key.right)
                 keyboard.release(Key.right)
                 keyboard.press(Key.backspace)
                 keyboard.release(Key.backspace)
                 keyboard.press(Key.backspace)
                 keyboard.release(Key.backspace)
                 driver.find_element(By.XPATH,
                                     '//*[@id="owl-dt-picker-0"]/div[2]/owl-date-time-timer/owl-date-time-timer-box[1]/label/input').send_keys(
                     str(s_time))
                 driver.find_element(By.XPATH, '//*[@id="owl-dt-picker-0"]/div[2]/div/button[2]/span').click()
             driver.find_element(By.XPATH,'//*[@id="addOffer2"]/div[1]/div/div[1]/div[1]/div/div[2]/div/label/span')
         elif pickup_option=="delivery":
             driver.find_element(By.XPATH,
                                 '//*[@id="addOffer2"]/div[1]/div/div[1]/div[1]/div/div[2]/div/label/span').click()
             #driver.find_element(By.XPATH,'//*[@id="addOffer2"]/div[1]/div/div[2]/div[1]/div/div[2]/div/label/span').click()
             driver.find_element(By.XPATH,'//*[@id="addOffer2"]/div[1]/div/div[2]/div[1]/div/div[2]/div/label/span').click()

        # pdb. set_trace()
         #checking time and writing time in fields



         # if s_time_check=="a":
         #     driver.find_element(By.XPATH,'//*[@id="basic-addon1"]').click()
         #     driver.find_element(By.XPATH,'//*[@id="owl-dt-picker-1"]/div[2]/owl-date-time-timer/div')
         #

         driver.find_element(By.XPATH, '//*[@id="addOffer2"]/div[1]/div/div[1]/div[2]/div[1]/div/input')
         # time.sleep(60)
         driver.find_element(By.XPATH, '//*[@id="post-menu"]/div/div/div[2]/div[4]/div/div/button').click()
         # time.sleep(15)
         driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]').click()
         print('Test case passed')
         f = open("C:\\Users\Arsal Azeem\\Desktop\\results.txt", "w")
         f.write("Test case passed")
         n=k
         n=n+1
         c1 = sheet2.cell(row=n, column=10)
         c1.value = "Pass"
         wb2.save(loc)
         #fdfsd
         a = str(i)
         dictname = "mydata" + "" + a
         dictname = {}
         dictname["dishname"] = dishname
         dictname["dishprice"] = price
         dictname["description"] = description
         dictname["order_type"]=pickup_option
         dictname["start time"]=s_time
         dictname["Ending time"]=e_time
         dictname["Dish Avaibility"]=avialbility
         dictname["testresult"]="passed"

         add_dish_result.append(dictname)
         #asdas
         driver.close()
    except:
        print('Adding Dish case failed')
        f = open("C:\\Users\Arsal Azeem\\Desktop\\results.txt", "w")
        f.write("Test case failed")
        f.close()
        n = k
        c1 = sheet2.cell(row=n + 1, column=10)
        c1.value = "Fail"
        wb2.save(loc)
        a = str(i)
        dictname = "mydata" + "" + a
        dictname = {}
        dictname["dishname"] = dishname
        dictname["dishprice"] = price
        dictname["description"] = description
        dictname["order_type"] = pickup_option
        dictname["start time"] = s_time
        dictname["Ending time"] = e_time
        dictname["Dish Avaibility"] = avialbility
        dictname["testresult"] = "failed"
        add_dish_result.append(dictname)
        driver.close()
    k=k+1


results_add_dish=json.dumps(add_dish_result)
print(results_add_dish)












