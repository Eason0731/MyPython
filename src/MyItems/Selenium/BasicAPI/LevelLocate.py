# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class LevelLocate(unittest.TestCase): #11
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testLevelLocate(self): 
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','level_locate.html')
        driver.get(URL)

        driver.find_element_by_link_text('Link1').click() #Click the Link1 to show the drop down list
        time.sleep(2)
    
        dropdownlist = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')#Find the 'Another action' on drop down list

        ActionChains(driver).move_to_element(dropdownlist).perform() #To move on this element
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
