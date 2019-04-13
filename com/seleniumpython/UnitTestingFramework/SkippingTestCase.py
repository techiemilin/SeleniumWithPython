'''
Created on Apr. 11, 2019

@author: milinpatel
'''
import unittest



class UnitTestExample(unittest.TestCase):
    
   
    
    
    @unittest.SkipTest
    def test_search(self):
        print("search")
    
    def test_advanceSearch(self):
        print("Advance search")
        
    def test_imageSearch(self):
        print("imange search")
    
    def test_contentSearch(self):
        print("Content Search")
        
        
if __name__ == "__main__":
    unittest.main()
        