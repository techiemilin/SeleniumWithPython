'''
Created on Apr. 11, 2019

@author: milinpatel
'''

from selenium import webdriver
from com.seleniumpython.excelFunctions.XLUtils import getRowCount, readData, writeData

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")

driver.get("http://newtours.demoaut.com")
driver.maximize_window()

path = "/Users/milinpatel/Documents/workspace/SeleniumWithPython/excelfiles/DataFileForDataDrivenTesting.xlsx"

rows = getRowCount(path, "Sheet1")

for r in range(2,rows+1):
    username = readData(path, "Sheet1",r,1)
    password = readData(path, "Sheet1", r, 2)
    
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    
    if driver.title==("Find a Flight: Mercury Tours:"):
        print("Test Passed")
        writeData(path, "Sheet1", r, 3,"Test Passed")
   
    else:
        print("Test Failed")
        writeData(path, "Sheet1", r, 3, "Test failed")