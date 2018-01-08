# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class HandleDropdownlist(unittest.TestCase): #13
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testHandleDropdownlist(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','drop_down.html')
        driver.get(URL)
        #Use search to click drop down list
        dropdownlist = driver.find_elements_by_tag_name('option')
        time.sleep(2)

        for mychoose in dropdownlist:
            if mychoose.get_attribute('value') == '10.69':
                mychoose.click()
        time.sleep(2)
        #Use search to click drop down list

        driver.find_element_by_id('ShippingMethod').find_element_by_xpath("//option[@value='7.45']").click() #Use level locate to click drop down list
        time.sleep(2)

        #Use two click step to select
        driver.find_element_by_id('ShippingMethod').click()
        time.sleep(2)
        driver.find_element_by_xpath("//option[@value='11.61']").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()
