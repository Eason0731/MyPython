# coding:utf-8
import unittest
import os
import time
from . import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class UseJavaScriptOnSogou(unittest.TestCase): #15.38
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testUseJavaScriptOnSogou(self): 
        driver = self.driver
        URL = 'http://www.sogou.com'
        driver.get(URL)
        Content = 'Hello Selenium'
        time.sleep(3)
    
        TitleName = driver.execute_script('return document.title')
        if '搜狗搜索引擎 - 上网从搜狗开始' == TitleName:
            print("Title name is correct!")
        else:
            print("Current title name is " + TitleName)

        SearchBox = driver.find_element_by_id('query')
        SearchButton = driver.find_element_by_id('stb')

        driver.execute_script('arguments[0].value = "'+ Content + '"',SearchBox) #Use js to input words on SearchBox .value = send_keys
        time.sleep(2)

        driver.execute_script('arguments[0].click()',SearchButton) #Click the button
        time.sleep(2)

        TitleName2 = driver.execute_script('return document.title')
        if Content + ' - 搜狗搜索' == TitleName2:
            print("Title name of search is correct!")
        else:
            print("Current title name is " + TitleName2)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()
