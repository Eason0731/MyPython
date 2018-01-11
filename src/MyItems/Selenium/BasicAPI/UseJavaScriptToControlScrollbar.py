# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class UseJavaScriptToControlScrollbar(unittest.TestCase): #19
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testUseJavaScriptToControlScrollbar(self): #19
        driver = self.driver
        URL = 'http://www.sogou.com'
        driver.get(URL)
        driver.find_element_by_id('query').send_keys('JavaScript')
        time.sleep(2)

        driver.find_element_by_id('stb').click()
        time.sleep(2)
    
        ScrollToBottom = 'window.scrollTo(0,document.body.scrollHeight)' #Scroll Bar move to bottom
        ScrollToTop = 'window.scrollTo(document.body.scrollHeight,0)' #Scroll Bar move to top
        ScrollUp = 'window.scrollTo(document.body.scrollHeight,500)' #Move up 500px
        ScrollDown = 'window.scrollTo(500,1500)' #Move down 300px
        #window.scrollTo(start,end) 
        driver.execute_script(ScrollToBottom)
        time.sleep(2)

        driver.execute_script(ScrollUp)
        time.sleep(2)

        driver.execute_script(ScrollDown)
        time.sleep(2)
    
        driver.execute_script(ScrollToTop)
        time.sleep(2)
        driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()
