import initchrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdb
k=0

def return_flags(links,search_word):
    global k
    temp = str(links)
    words=temp.split()
    for word in words:
        if word==search_word:
            k = k + 1
    return k

def search_whole_page(url,word_to_search):
    driver = initchrome.start()
    url = url
    driver.get(url)
    count = 0
    # temp=driver.find_elements(By.TAG_NAME,"p").text
    # for i in temp:
    #     print(i)
    for a in driver.find_elements(By.XPATH, '*'):
        try:
            links = a.text
            # To raise flag against target word
            return_flags(links, word_to_search)
            #
            # print(links)

        except Exception as e:
            driver.quit()
            print(e)
    return int(k)

def find_word_on_page(url,word_to_search):
    driver = initchrome.start()
    url = url
    driver.get(url)
    count = 0
    # temp=driver.find_elements(By.TAG_NAME,"p").text
    # for i in temp:
    #     print(i)
    for a in driver.find_elements(By.TAG_NAME, 'p'):
        try:
            links = a.text
            # To raise flag against target word
            return_flags(links,word_to_search)
            #
            # print(links)

        except Exception as e:
            driver.quit()
            print(e)
    # text = driver.find_element_by_xpath('//*[@id="privacy_div"]/div/div/div/div[1]/div/div/div/div/div[2]/p[1]').text
    # print(text)
    driver.quit()
    print("Total occurances ", str(k))
    return int(k)

def search_word(url,word_to_search):
    if word_to_search.lower()==word_to_search:
        capital_word = word_to_search.capitalize()
        user_word = word_to_search
        print("Results for word: " + word_to_search)
        find_word_on_page(url, user_word)
        print("Results for word: " + capital_word)
        find_word_on_page(url, capital_word)
    else:
        print("Results for word: " + word_to_search)
        find_word_on_page(url,word_to_search)

def search_word_on_whole_page(url,word_to_search):
    if word_to_search.lower() == word_to_search:
        capital_word = word_to_search.capitalize()
        user_word = word_to_search
        print("Results for word: " + word_to_search)
        search_whole_page(url, user_word)
        print("Results for word: " + capital_word)
        find_word_on_page(url, capital_word)
    else:
        print("Results for word: " + word_to_search)
        search_whole_page(url, word_to_search)
        return int(k)

