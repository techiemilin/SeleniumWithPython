'''
Created on Apr. 11, 2019

@author: milinpatel
'''

#===============================================================================
# debug
# Info and warning
# Error and Critical 
#===============================================================================



import logging



logging.basicConfig(filename="/Users/milinpatel/Documents/workspace/SeleniumWithPython/com/seleniumpython/test.log",
                    format= "%(asctime)s: %(levelname)s: %(message)s",
                    datefmt= "%m/%d/%y %i:%M:%s %p", level = logging.DEBUG)


logging.debug("This is debug messege")
logging.info("This is debug messege")
logging.warning("This is warning messege")
logging.error("This is error messege")
logging.critical("This is critical messege")
