'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("https://www.facebook.com/")

textbox = driver.find_element_by_xpath("//input[@id = 'email']")

action = ActionChains(driver)
action.context_click(textbox).perform()

time.sleep(2)

driver.close()

