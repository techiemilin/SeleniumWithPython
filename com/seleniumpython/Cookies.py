'''
Created on Apr. 11, 2019

@author: milinpatel
'''

from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://www.amazon.ca/")

cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# adding cookie 

cookie = {"name" : "My cookie"}
driver.add_cookie(cookie)
driver.get_cookies

print(driver.get_cookies)
print(len(driver.get_cookies))

driver.delete_all_cookies()
