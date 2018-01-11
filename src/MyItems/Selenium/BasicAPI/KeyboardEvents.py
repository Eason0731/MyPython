# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.common.keys import Keys #Need to import package Keys

class KeyboardEvents(unittest.TestCase): #8
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testKeyboardEvents(self):
        driver = self.driver
        URL = 'http://www.baidu.com'
        driver.get(URL)
        driver.find_element_by_id('kw').send_keys("Hello Selenium")
        time.sleep(3)

        driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE) #Backspace
        time.sleep(3)

        driver.find_element_by_id('kw').send_keys(Keys.SPACE) #Space
        time.sleep(3)
    
        driver.find_element_by_id('kw').send_keys(Keys.DELETE) #Delete
        driver.find_element_by_id('kw').send_keys('20170808')
        time.sleep(3)

        driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a') # CTRL + A
        time.sleep(3)

        driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x') # CTRL + X
        time.sleep(3)

        driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v') # CTRL + V
        time.sleep(3)
    
        driver.find_element_by_id('kw').send_keys(Keys.ENTER) #ENTER
        time.sleep(3)
        
        #driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c') # CTRL + C
        #driver.find_element_by_id('kw').send_keys(Keys.TAB) # TAB

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
