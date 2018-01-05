# coding:utf-8
import unittest
import os
import time
from . import Getbrowser
import sys

class GetSomeAttributes(unittest.TestCase): #5
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testGetSomeAttributes(self): 
        driver = self.driver
        URL = 'http://www.baidu.com'
        driver.get(URL)
        print(driver.find_element_by_id('kw').size) # get the size of search box
        time.sleep(2)
        print(driver.find_element_by_id('jgwab').text) # get the text on this link
        time.sleep(2)
        print(driver.find_element_by_id('su').get_attribute('type')) # get the type of search button
        time.sleep(2)
        print(driver.find_element_by_name('wd').is_displayed()) #to judge whether this element is display or not

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()
