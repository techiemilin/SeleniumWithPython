'''
Created on Apr. 9, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title

user_name = driver.find_element_by_name("userName")

password_box = driver.find_element_by_name("password")

user_name.send_keys("mercury")
password_box.send_keys("mercury")

btn = driver.find_element_by_name("login")
btn.click()

driver.close()
