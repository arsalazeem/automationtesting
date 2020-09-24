from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import variable_names
import time
import string
import initchrome
import random
import initmozzile
import pdb
import json
import post_data
from datetime import datetime
import datetime
from datetime import date
import requests
from selenium import webdriver


url_list=[]
datalist=[]
total_lenght=12
record_list=[]


def _append_check_advanced(lists):
    checklist=['apps','play','apple','twitter','facebook','instagram','store','apple','google','amazon']
    output = any([substring in lists for substring in checklist])
    if output:
        print("This is not my job")
    else:
        url_list.append(lists)

def _checklast(name):
    if name[-1]=="/":
        return True
    else:
        return False

def check_duplicates(a):
    for a_link in record_list:
        if a_link==a:
            return True
            break

def _return_status_code(code):
    s_messege=" "
    if code>199 and code<400:
        s_messege=variable_names.statuscodepassed
    else:
        s_messege=variable_names.statuscodefailed
    return s_messege


def _get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



def _toJson(a):
    return json.dumps(a, default=lambda o: o.__dict__)

def _check_broken_links(page_url):
    total=0
    fail=0
    # jsonlist["page_url"]=page_url
    t_time = datetime.datetime.now().strftime("%H:%M:%S")
    # jsonlist["current_time"]=t_time
    print("i am here")
    driver=initchrome.start()
    print(page_url)
    driver.get(page_url)
    driver.implicitly_wait(30)
    # links=driver.find_elements_by_css_selector("a")
    # elem = driver.find_elements_by_xpath("//*[@href]")
    # print(elem)
    # # for link in links:
    # #     r = requests.head("https://dev.tradishes.com/home.html")
    # #     print(r)
    for a in driver.find_elements_by_xpath('.//a'):
        total=total+1
        # temp_dict="temp_dict"+str(n)
        try:
            links = a.get_attribute('href')

            if check_duplicates(links):
                return 0,0
            if _checklast(links):
                links=links[:-1]
                print("I have trimmed:",links)
            _append_check_advanced(links)
            record_list.append(links)
            r = requests.head(links)
            s_code=int(r.status_code)
            # if r!='<Response [404]> ':
            #     status="passed"
            # else:
            #     status=" broken"
            # if "twitter" in links:
            #     print(links)
            #     print("Do nothing with jsonlist")
            # if "instagram" in links:
            #     print(links)
            #     print("Do nothing with jsonlist")
            # else:
            temp_dict=_get_random_string(8)
            temp_dict={}
            temp_dict[variable_names.url]=links
            temp_dict[variable_names.code]=s_code
            temp_dict[variable_names.status]=_return_status_code(s_code)
            datalist.append(temp_dict)
            # jsonlist[links + " " + "status"] = r.ok
            # print(links + ' ' + str(r.ok))
            if str(r.ok) == "False":
                # print(k)
                fail=fail+1
        except Exception as e:
            print("This a tag contains no URL",e)


    # if k>0:
    #     result=variable_names.failed
    # else:
    #     result= variable_names.passed



    driver.quit()
    return total,fail







def _check_list_urls(total, fail, pass_list, page_url, testname, description, p_name):
    t=total
    f=fail
    try:
        for a in pass_list:
            result=_check_broken_links(a)
            total_scanned=result[0]
            total_failed=result[1]
            t=total_scanned+t
            f=total_failed+f
    except Exception as e:
        print(e)
    print("Total scanned:",t)
    print("Total failed:",f)
    if f>0:
        result=variable_names.failed
    else:
        result=variable_names.passed
    #
    mainlist={}
    mainlist[variable_names.sample_values]=""
    mainlist[variable_names.currenttime]=str(variable_names.get_time())
    mainlist[variable_names.pageurl]=page_url
    mainlist[variable_names.innerdata]=datalist
    mainlist[variable_names.totalcount]=str(t)
    mainlist[variable_names.totalfailed] = str(f)
    mainlist[variable_names.actualresult]=result
    mainlist[variable_names.expectedresult]=variable_names.passed
    #
    post_data.post_data_on_portal(mainlist,testname,description,p_name)







def brokenlinks_post(url,project_name):
    test = "Check Broken Links"
    description = "To check weather there are any broken links on a site or not"
    url = url
    project_name = project_name
    test = test
    description = description
    n_data = _check_broken_links(url)
    a_total = n_data[0]
    f_total = n_data[1]
    templist = url_list
    final_list = list(dict.fromkeys(templist))
    _check_list_urls(a_total, f_total, final_list, url, test, description, project_name)


url="https://www.pointx.me/"
project_name="PointX"

brokenlinks_post(url,project_name)






#brokenlinks_post() is the main method that control other method.Please don't call any other method seperaterly.

# brokenlinks_post()
