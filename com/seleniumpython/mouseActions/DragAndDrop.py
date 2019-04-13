'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element_by_xpath("//*[@id = 'box6']")
target_element = driver.find_element_by_xpath("//*[@id='box106']")

action = ActionChains(driver)

action.drag_and_drop(source_element, target_element).perform()

time.sleep(3)

driver.close()
