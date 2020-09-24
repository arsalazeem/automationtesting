import time

def check_empty(driver):
    time.sleep(5)
    try:
        homescreen_element = driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[5]')
        print(homescreen_element.get_attribute("text"))
        homescreen_element = homescreen_element.is_displayed()
        if homescreen_element:
            print(homescreen_element)
            return homescreen_element

        else:
            print(homescreen_element)
            return homescreen_element
    except Exception as e:
        return False
