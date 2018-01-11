# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait

class LocateFrame(unittest.TestCase): #12
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testLocateFrame(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','frame.html')
        driver.get(URL)

        driver.switch_to_frame('f1') # switch to frame named f1

        driver.switch_to_frame('f2') # switch to frame named f2

        driver.find_element_by_name('wd').send_keys('Hello Selenium') #Find the element on the frame then operate it
        driver.find_element_by_id('su').click()
        time.sleep(3)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
