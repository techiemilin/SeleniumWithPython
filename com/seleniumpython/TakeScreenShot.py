'''
Created on Apr. 11, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("https:/www.google.com")

driver.save_screenshot("/Users/milinpatel/Documents/workspace/SeleniumWithPython/com/screenshot"+".png")

driver.get_screenshot_as_file("/Users/milinpatel/Documents/workspace/SeleniumWithPython/com/screenshot1"+".png")

driver.close()
