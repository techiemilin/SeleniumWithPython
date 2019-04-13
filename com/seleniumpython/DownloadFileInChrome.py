'''
Created on Apr. 10, 2019

@author: milinpatel
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chromeOptions = Options()
# chromeOptions.experimental_options("prefs", {"download.default_directory": "/milinpatel⁩/downloads/ClassExamples"})

driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")  # ,chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_xpath("//textarea[@id = 'textbox']").send_keys("Selenium WebDriver with Python by Milin")

driver.find_element_by_xpath("//button[@id = 'createTxt']").click()

driver.find_element_by_xpath("//a[@id = 'link-to-download']").click()

# PDF download

driver.find_element_by_xpath("//textarea[@id = 'pdfbox']").send_keys("Selenium WebDriver with Python by Milin")

driver.find_element_by_xpath("//button[@id = 'createPdf']").click()

driver.find_element_by_xpath("//a[@id = 'pdf-link-to-download']").click()

