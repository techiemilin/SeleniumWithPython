'''
Created on Apr. 9, 2019

@author: milinpatel
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/geckodriver ")

driver.get("http://www.google.com")

s = driver.title

print(s)
driver.maximize_window()
driver.minimize_window()
driver.close()
