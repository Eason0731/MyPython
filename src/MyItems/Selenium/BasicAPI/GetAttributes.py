# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class GetAttributes(unittest.TestCase): #20
    def setUp(self):
        self.driver = Getbrowser.Chrome()

    def testGetAttributes(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','GetAttributes.html')
        driver.get(URL)

        Checkboxs = driver.find_elements_by_css_selector('input[type=checkbox]')
        for mycheckbox in Checkboxs:
            if mycheckbox.get_attribute('data-node') == '594434498':
                mycheckbox.click()
        
            if mycheckbox.get_attribute('data-convert') == '1':
                mycheckbox.click()
                time.sleep(2)
        
            if mycheckbox.get_attribute('data-type') == 'file':
                mycheckbox.click()
                time.sleep(2)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()
