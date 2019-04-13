'''
Created on Apr. 9, 2019

@author: milinpatel
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")

user_name = driver.find_element_by_name("userName")

password_box = driver.find_element_by_name("password")

user_name.send_keys("mercury")
password_box.send_keys("mercury")

btn = driver.find_element_by_name("login")
btn.click()

radio_button = driver.find_element_by_css_selector("input[value = roundtrip]")
status = radio_button.is_selected()
print(status)

radio_button1 = driver.find_element_by_css_selector("input[value = oneway]")
status1 = radio_button1.is_selected()
print(status1)

time.sleep(3)

driver.close()
