'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("http://newtours.demoaut.com")

all_links = driver.find_elements_by_tag_name("a")
print("total links :-" , len(all_links))

for links in all_links:
    print(links.text)
    
driver.find_element_by_link_text("Hotels").click()

driver.back()

driver.find_element_by_partial_link_text("alon").click()

driver.close()
