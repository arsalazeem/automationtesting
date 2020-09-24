import initchrome


driver=initchrome.start()
driver.get("https://dev.kardkey.com/#/")
driver.implicitly_wait(30)
driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[1]/div[1]/div/div[1]/button').click()
driver.find_element_by_xpath('/html/body/app-root/app-product/div/div[1]/div[1]/div[3]/div/div/div/div[4]/button[2]/span[1]').click()
driver.find_element_by_xpath('//*[@id="cart"]').click()
temp=driver.find_element_by_xpath('//*[@id="desktop"]/div[2]/div[3]/div/div[2]/div/input').get_attribute("value")
temp=driver.find_element_by_xpath('//*[@id="desktop"]/div[2]/div[7]/div[2]/h4').get_attribute("value")
print(temp)


