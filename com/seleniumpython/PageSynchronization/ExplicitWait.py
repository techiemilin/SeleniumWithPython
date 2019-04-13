'''
Created on Apr. 9, 2019

@author: milinpatel
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.expedia.ca/")

driver.find_element_by_id("tab-flight-tab-hp").click()

driver.find_element_by_id("flight-origin-hp-flight").send_keys(" JFK")

driver.find_element_by_id("flight-destination-hp-flight").send_keys(" YYZ")

driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/06/2019")

# driver.find_element_by_id("flight-returning-hp-flight").click()
driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("15/06/2019")

driver.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']//button[contains(@type,'submit')]").click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "stopFilter_stops-0")), "myDynamicElement").click()
time.sleep(3)

driver.quit()
