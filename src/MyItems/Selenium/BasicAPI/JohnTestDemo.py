# -*- coding: cp936 -*-
import os
import unittest
from . import Getbrowser
import time
from selenium import webdriver

#This is a standard python selenium case with unittest framework
#Once I forgot the structure then open this file to recall

class JohnTestDemo(unittest.TestCase): #class function to write the test case function with unittest framework
    def setUp(self): #setUp is a initial function which should call browser
        self.driver = Getbrowser.Chrome()

    def testJohnTestDemo(self): #Test case program and should named start with 'test' for any test cases name
        driver = self.driver
        #This function to open sogou page then verify the page title
        Sogou = 'http://www.sogou.com'
        driver.get(Sogou)
        time.sleep(2)
        self.assertIn('搜狗搜索引擎 - 上网从搜狗开始',driver.title)
        time.sleep(2)
        #This function to open sogou page then verify the page title

    def tearDown(self):#tearDown is a final function which should cloase browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main() #The main function of unittest will call the unittest.TestCase on current file then execute the test case
        
