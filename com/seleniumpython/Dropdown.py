'''
Created on Apr. 10, 2019

@author: milinpatel
select one option
capture options from drop down
count how many options are present
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?153770259640")

dropdown = driver.find_element_by_id("RESULT_RadioButton-7")

select = Select(dropdown)

select.select_by_visible_text("Morning")

select.select_by_index(2)

select.select_by_value("Radio-2")

time.sleep(2)

# capture all the option in drop down
drp = select.options
print(len(drp))


# print all options by for loop
for i in drp:
    print(i.text)
time.sleep(2)
driver.close()
