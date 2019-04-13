'''
Created on Apr. 9, 2019

@author: milinpatel

'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("http://www.google.com")
driver.maximize_window()




page_source = driver.page_source
print(page_source)


s = driver.title
print(s)

driver.close()
