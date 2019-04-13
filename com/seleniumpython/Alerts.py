'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver

import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element_by_name("proceed").click()
time.sleep(2)

alert_text = driver.switch_to.alert

alert_text.accept()
print(alert_text.text)
time.sleep(2)

driver.close()

