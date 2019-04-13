'''
Created on Apr. 10, 2019

@author: milinpatel
'''

from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Capabilities").click()

driver.back()

driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium")

driver.close()
