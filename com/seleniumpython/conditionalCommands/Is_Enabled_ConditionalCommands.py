'''
Created on Apr. 9, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")

user_name = driver.find_element_by_name("userName").is_enabled()

password_box = driver.find_element_by_name("password").is_enabled()


print(user_name)

print(password_box)

driver.close()
