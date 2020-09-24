from src.testproject.sdk.drivers import webdriver
from src.testproject.sdk.drivers.actions.webactions import web_actions

def start(mobileid):
    # baf8c2f7
    desired_capabilities = {
            "appActivity": "com.lock.till.MainActivity",
            "appPackage": "com.lock.till",
            "udid": mobileid,
            "browserName": "",
            "platformName": "Android"
        }
    driver = webdriver.Remote(token='MPENCENWGnNwy7E3OhgOucsCYRoiQXAO37dtNXA3StQ1',desired_capabilities=desired_capabilities)
    return driver

