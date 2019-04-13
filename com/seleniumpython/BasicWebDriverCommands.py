'''
Created on Apr. 9, 2019

@author: milinpatel
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get ("http://www.google.com")

title = driver.title
print("Title of the page :- " + title)

current_url = driver.current_url
print("Current URL of the Page is :- " + current_url)

driver.find_element_by_name("q").send_keys("Milin")
driver.find_element_by_link_text("About").click()

time.sleep(3)

#driver.close()

driver.quit()

