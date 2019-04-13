'''
Created on Apr. 10, 2019

@author: milinpatel


Mouse Actions : - mouse over
                 hover-over
                 drag and drop
                 click, 
                 right click
                 double click

'''
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath("//input[@id = 'txtUsername']").send_keys("Admin")

driver.find_element_by_xpath("//input[@id = 'txtPassword']").send_keys(("admin123"))

driver.find_element_by_xpath("//input[@id = 'btnLogin']").click()

Admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
UserManagement = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_id("menu_admin_viewSystemUsers")

action = ActionChains(driver)
action.move_to_element(Admin).move_to_element(UserManagement).move_to_element(users).click().perform()

driver.close()
