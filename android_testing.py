from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions.webactions import web_actions
import time
import pdb
import variable_names
import post_data
import lock_enter_pin

jsonlist=[]


def test_hybrid_android_app():
    desired_capabilities = {
        "appActivity": "com.lock.till.MainActivity",
        "appPackage": "com.lock.till",
        "udid": "baf8c2f7",
        "browserName": "",
        "platformName":"Android"
    }
    try:
        exception="none"
        total=0
        fail=0
        email="arsal11210@yopmail.com"
        password="12345678"
        tempict={}
        driver = webdriver.Remote(token='MPENCENWGnNwy7E3OhgOucsCYRoiQXAO37dtNXA3StQ1',desired_capabilities=desired_capabilities)
        driver.reset()
        total=total+1
        driver.implicitly_wait(40)
        for i in range(1,3):
            time.sleep(30)
            driver.swipe(991, 1511, 99, 1517, 4559)
        coordinates=(500,1523)
        driver.tap(coordinates)
        # driver.tap((500, 1523))
        # tempict[variable_names.pageurl]=desired_capabilities["appPackage"]
        tempict[variable_names.formname]=desired_capabilities["appPackage"]
        tempict["Email"]=email
        tempict["Password"]=password
        tempict[variable_names.expectedresult]=variable_names.passed
        print("I am here")
        # time.sleep(40)
        driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.EditText[1]').send_keys(email)
        driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.EditText[1]').send_keys(password)
        driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[5]/android.widget.Button[1]').click()
        driver=lock_enter_pin.enter_pin(driver,"123456")

        try:
            homescreen_element=driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[5]')
            if homescreen_element:
                result=variable_names.passed
                tempict[variable_names.actualresult]=result
                # return result
        except Exception as e:
            exception="none"
            result=variable_names.failed
            tempict[variable_names.actualresult] = result
            fail=fail+1

            # return result



    except Exception as e:
        print(str(e))
    tempict[variable_names.n_exception]=exception
    tempict[variable_names.totalcount]=str(total)
    tempict[variable_names.totalfailed]=str(fail)
    jsonlist.append(tempict)
    mainlist={}
    page_url = "https://dev.kardkey.com/#/"
    mainlist[variable_names.sample_values] = jsonlist
    mainlist[variable_names.currenttime] = variable_names.get_time()
    mainlist[variable_names.pageurl] = desired_capabilities["appPackage"]
    mainlist[variable_names.innerdata] = ""
    mainlist[variable_names.totalcount] = str(total)
    mainlist[variable_names.totalfailed] =str(fail)
    mainlist[variable_names.actualresult] = ""
    mainlist[variable_names.expectedresult] = ""
    print(mainlist)

    project_list=variable_names.show_project_name()
    id=project_list[0]
    project_name=project_list[1]
    print("I am using this info: ",id,project_name)
    pdb.set_trace()
    post_data.post_data_on_portal(mainlist,"Login","To check weather user is able to login with a valid email and password",project_name,id)






test_hybrid_android_app()