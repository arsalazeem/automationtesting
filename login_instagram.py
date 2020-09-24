# import requests
# import json
import initchrome
# import initdriver
def driver_click(driver,path):
    driver.find_element_by_xpath("'"+path+"'").click()
#
def login_insta():
    print("This is Instagram login Module,")
    print("Please enter your email and password")
    # email=input()
    # password=input()
    email = "arsalazeem101@gmail.com"
    password = "123456"
    driver = initchrome.start()
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    return driver

# driver=initdriver.start()
# driver.get("https://dev.tradishes.com/#/host/register")
# driver.find_element_by_xpath('//*[@id="email"]').send_keys("azeemarsal@gmail.com")