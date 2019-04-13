'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame("frame-one1434677811")

upload_box = driver.find_element_by_xpath("//input[@id = 'RESULT_FileUpload-11']")

upload_box.send_keys("‎⁨/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ⁩")
