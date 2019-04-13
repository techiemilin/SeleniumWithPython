'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

btn = driver.find_element_by_xpath("//button[@ondblclick = 'myFunction1()']")




action = ActionChains(driver)
action.double_click(btn).perform()
time.sleep(3)

time.sleep(3)

driver.close()

