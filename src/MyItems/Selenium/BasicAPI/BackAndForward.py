# coding:utf-8
import unittest
import os
import time
from . import Getbrowser
import sys

class BackAndForward(unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testBackAndForward(self): #2
        driver = self.driver
        #driver = Getbrowser.Chrome()
        URL1 = 'http://www.baidu.com'
        URL2 = 'http://www.sogou.com'
        driver.get(URL1)
        time.sleep(2)
        print("Now go to website: " + URL1)
        driver.get(URL2)
        time.sleep(2)
        print("Now go to website: " + URL2)
        driver.back() #Back to URL1
        time.sleep(2)
        print("Now back to website: " + URL1)
        driver.forward() #Forward to URL2
        time.sleep(2)
        print("Now forward to website: " + URL2)
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
