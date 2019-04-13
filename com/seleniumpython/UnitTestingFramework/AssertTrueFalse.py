'''
Created on Apr. 11, 2019

@author: milinpatel
'''
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    
    def test_1(self):
        self.driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(5)
        
        self.driver.get("https://www.google.com")
        
        Webpage_title = self.driver.title
        
        self.assertTrue(Webpage_title=="Google", "passed")
        self.driver.close()
        
    def test_2(self):
        self.driver = webdriver.Chrome("/Users/milinpatel/Documents/workspace/SeleniumWithPython/drivers/chromedriver ")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(5)
        
        self.driver.get("https://www.google.com")
        
        Webpage_title = self.driver.title
        
        self.assertFalse(Webpage_title=="Google", "failed")
        self.driver.close
        
if __name__ == "__main__":
    unittest.main()