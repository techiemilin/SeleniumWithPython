'''
Created on Apr. 11, 2019

@author: milinpatel
'''
import unittest
from selenium import webdriver


class SearchPage(unittest.TestCase):
   
    def test_google(self):
        self.driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(5)
        
        self.driver.get("https://www.google.com")
        
        print(self.driver.title)
        
        self.driver.close()
        
    def test_yahoo(self):
        
        self.driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(5)
        
        self.driver.get("https://ca.search.yahoo.com/")
        
        print(self.driver.title)
        
        self.driver.close()

        
if __name__ == "__main__":
    unittest.main()
        
