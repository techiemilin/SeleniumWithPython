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
        
        actual_title = self.driver.title
        
        expected_title = "Google"
        
        self.assertAlmostEqual(expected_title, actual_title, "Title is not match")
        
        
if __name__ == "__main__":
    unittest.main()
        
    
