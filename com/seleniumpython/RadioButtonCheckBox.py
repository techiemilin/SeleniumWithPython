'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://www.facebook.com/")

female_btn = driver.find_element_by_id("u_0_9")

if female_btn.is_selected():
    print(female_btn)
else:
    female_btn.click()

male_btn = driver.find_element_by_id("u_0_a").is_selected()
print(male_btn)

driver.get("http://www.echoecho.com/htmlforms09.htm")

opt1 = driver.find_element_by_name("option1")
if opt1.is_selected():
    print("is selected")
else: opt1.click()

opt2 = driver.find_element_by_name("option2")
if opt2.is_selected():
    print("is selected")
else: opt2.click()

opt3 = driver.find_element_by_name("option3")
if opt3.is_selected():
    print("is selected")
else: opt3.click()

time.sleep(3)

