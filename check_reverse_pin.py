import create_notes
import android_login
import time
import variable_names
import post_data

total = 1
fail = 0
exception = "none"
# creation of notes
email = "arsal11210@yopmail.com"
password = "12345678"
pin = "654321"
try:
    driver = create_notes.create_notes(1)
except Exception as e:
    print(e)

# below lines will reset the app,login the app and will enter a reverse PIN. valid login takes three parameters ->email,password and pin.
try:
    driver = android_login.valid_login("arsal11210@yopmail.com", "12345678", "654321")
    homescreen_element = driver.find_element_by_xpath(
        '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[5]')
    homescreen_element = homescreen_element.is_displayed()
    if homescreen_element:
        print(homescreen_element)
        result=variable_names.passed
    else:
        fail = 1
        print(homescreen_element)
        result=variable_names.failed
except Exception as e:
    print(e)
    exception = str(e)

sample_values = {"form-name": "Locktill Login", "email": email, "password": password, "pin": pin,
                 variable_names.n_exception: exception, variable_names.totalcount: str(total),
                 variable_names.totalfailed: str(fail), variable_names.expectedresult: variable_names.passed,
                 variable_names.actualresult: result}
jsonlist = [sample_values]
mainlist = {}
mainlist[variable_names.sample_values] = jsonlist
mainlist[variable_names.currenttime] = variable_names.get_time()
mainlist[variable_names.pageurl] = "com.lock.till"
mainlist[variable_names.innerdata] = ""
mainlist[variable_names.totalcount] = str(total)
mainlist[variable_names.totalfailed] = str(fail)
mainlist[variable_names.actualresult] = ""
mainlist[variable_names.expectedresult] = ""

#posting data on portal
list=variable_names.show_project_name()
id=list[0]
project_name=list[1]
post_data.post_data_on_portal(mainlist,"Reverse PIN security","To check that reverser PIN security feautre is working properly or not",project_name,id)

