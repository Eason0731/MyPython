# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class MouseEvents(unittest.TestCase): #7
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testMouseEvents(self):
        driver = self.driver
        URL = 'http://www.baidu.com'
        driver.get(URL)
        ActionChains(driver).context_click(driver.find_element_by_id('kw')).perform() # context_click() can right click ,perform() means execute
        time.sleep(3)
        ActionChains(driver).double_click(driver.find_element_by_id('kw')).perform() # double_click() can dobule click ,perform() means execute
        time.sleep(3)
        ActionChains(driver).drag_and_drop(driver.find_element_by_id('kw'),driver.find_element_by_id('su')).perform() # drag_and_drop(source,target) can move from source to target ,perform() means execute
        time.sleep(3)
        ActionChains(driver).move_to_element(driver.find_element_by_id('kw')).perform() # move_to_element() can stop on target element ,perform() means execute
        time.sleep(3)
        ActionChains(driver).click_and_hold(driver.find_element_by_id('su')).perform() # click_and_hold() can click and hold on target element ,perform() means execute
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
