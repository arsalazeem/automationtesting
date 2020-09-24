import initchrome
import initmozzile
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys



def browser_results(url):
    firefox_driver = initmozzile.start()
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    driver.get("https://www.krypterro.com")

browser_results("https://dev.gardne.com/")