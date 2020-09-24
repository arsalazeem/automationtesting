import android_login
import time


def create_notes(numberofnotes):
    driver = android_login.valid_login("arsal11210@yopmail.com", "12345678", "123456")
    try:
        for i in range(1, numberofnotes + 1):
            driver.implicitly_wait(50)
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.Image[1]').click()
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[5]/android.widget.Image[1]').click()
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.app.Dialog[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.EditText[1]').send_keys(
                "note titile")
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.app.Dialog[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.widget.EditText[1]').send_keys(
                "note description")
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.app.Dialog[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.Image[1]').click()
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.app.Dialog[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Image[1]').click()
            driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.app.Dialog[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]').click()
            if i == numberofnotes + 1:
                return driver
    except:
        return driver