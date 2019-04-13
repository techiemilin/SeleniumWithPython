'''
Created on Apr. 13, 2019

@author: milinpatel
'''

import pytest

@pytest.yield_fixture()
def testMethod1(self):
    print("this is test method 1")
    yield
    print("Once ")
    


