'''
Created on Apr. 9, 2019

@author: milinpatel
'''

from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("https://www.facebook.com")
print(driver.title)

driver.get("https://www.google.com")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.refresh()
print(driver.title, "Page Refreshed")

driver.quit()
