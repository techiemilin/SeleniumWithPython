'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
# print(driver.current_window_handle) #CDwindow-A0CFA654C1DE256DA6B4B8DDE63053B7

# driver.switch_to_window("CDwindow-A0CFA654C1DE256DA6B4B8DDE63053B7")

all_windows = driver.window_handles

for i in all_windows:
    driver.switch_to.window(i)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()
    
driver.quit()
