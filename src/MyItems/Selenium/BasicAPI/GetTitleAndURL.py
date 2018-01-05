# coding:utf-8
import unittest
import os
import time
from . import Getbrowser
import sys

class GetTitleAndURL(unittest.TestCase): #1
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testGetTitleAndURL(self): 
        driver = self.driver
        driver.get('http://www.baidu.com')
        time.sleep(2)
        if '百度一下，你就知道' in driver.title: # "driver.title" to get the page title name on current page
            print("Pass: " + sys._getframe().f_code.co_name)
        else:
            print("Current page title is " + driver.title)
        print(driver.current_url) # "current_url" to get the page title URL address on current page
        print(driver.page_source) # "page_source" to get the page source on current page

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()
