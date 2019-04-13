'''
Created on Apr. 11, 2019

@author: milinpatel
'''
#===============================================================================
# setup() before every test_ method
# teardown() after every test_method
# setUpClass () once before 
# tearDownClass one after 

'''
setUpModule()
setUpClass()

SetUpMethod
Method()
tearDownMethod()

SetUpMethod
Method()
tearDownMethod()

SetUpMethod
Method()
tearDownMethod()

tearDownClass()
teardownModule()


'''

#===============================================================================

import unittest


class UnitTestExample(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        ("one time before the execution%%%%%%")
        
    @classmethod
    def tearDownClass(cls):
        ("one time after the execution%%%%%%")
    
    @classmethod
    def setUp(self):
        print("this is setUp method")
    
    @classmethod
    def tearDown(self):
        print("this is teadDown method")

    def test_search(self):
        print("search")
    
    def test_advanceSearch(self):
        print("Advance search")
        
    def test_imageSearch(self):
        print("imange search")
    
    def test_contentSearch(self):
        print("Content Search")
