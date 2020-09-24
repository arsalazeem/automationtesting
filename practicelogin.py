from urllib.request import urlopen
import initchrome
import urllib.request
import variable_names
import post_data
import requests
import pdb
from selenium.webdriver.common.by import By
from datetime import datetime
import datetime

import time
#
# myURL = urlopen("http://tradishes.com/")
t_time = datetime.datetime.now().strftime("%H:%M:%S")
images_list=[]
def return_status_code(code):
    print(code)
    s_messege=" "
    if code>199 and code<400:
        s_messege=variable_names.statuscodepassed
    else:
        s_messege=variable_names.statuscodefailed
    return s_messege
# print(myURL.read())
def check_broken_images(url):
    broken_url="none"
    k = 0
    massege = variable_names.passed
    driver = initchrome.start()
    driver.get(url)
    a = driver.find_elements(By.TAG_NAME, 'img')
    images_count=len(a)
    for i in a:
        temp_dict="temp_dict"+str(i)
        temp_dict={}
        try:
            link = i.get_attribute("src")
            response = requests.get(link)
            status = response.status_code
            temp_dict[variable_names.url]=link
            temp_dict[variable_names.code]=status
            temp_dict[variable_names.status]=return_status_code(int(status))
            images_list.append(temp_dict)
            if status != 200:
                massege = variable_names.failed
                k = k + 1
                broken_url=link
        except Exception as e:
            #massege = "Failed due to Exception:" + str(e)
            print(e)

    print(massege + ":" + str(k))
    return k,massege,url,images_count,str(broken_url)
url="https://www.enabling.systems/"
project_name="Enabling System"
result=check_broken_images(url)
occurances=result[0]
test_result=result[1]
page_url=result[2]
image_count=result[3]
broken_url=result[4]


#
datalist={}

# datalist["broken_url"]=broken_url
mainlist={}
mainlist[variable_names.sample_values]=""
mainlist[variable_names.currenttime]=variable_names.get_time()
mainlist[variable_names.pageurl]=page_url
mainlist[variable_names.innerdata]=images_list
mainlist[variable_names.totalcount]=image_count
mainlist[variable_names.totalfailed]=occurances
mainlist[variable_names.actualresult]=test_result
mainlist[variable_names.expectedresult]=variable_names.passed
post_data.post_data_on_portal(mainlist, "Broken Images Check", "To Check whether there are any broken images on prvoided webpage", project_name)

#



    # requests.get(link)
#
# driver=initchrome.start()
# n=0
# try:
#     driver.get("https://tradishes.com/")
#     # for i in range(1,30):
#     #     time.sleep(1)
#     #     driver.execute_script("window.scrollTo(0, 1080)")
#
#     a = driver.find_elements_by_tag_name('img')
#     for i in a:
#         url = "C:\\Users\\ENSX-PC\Desktop\\download_pics\\"
#         pic = i.get_attribute("src")
#         response=requests.get(pic)
#         print(response.status_code)
#         pdb.set_trace()
#         print(pic)
#         print("*****")
#         print(n)
#         urllib.request.urlretrieve(pic, url + str(n) + ".png")
#         n = n + 1
# except Exception as e:
#     driver.quit()
#     print(e)

