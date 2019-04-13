'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?153770259640")

# how many input boxes on the page and use send_keys() to enter the text, before entering the text use clear() to erase the text in the box
input_box = driver.find_elements_by_class_name("text_field")

print(len(input_box))

driver.close()
