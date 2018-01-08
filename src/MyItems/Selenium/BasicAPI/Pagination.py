# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class Pagination(unittest.TestCase): #14
    def setUp(self):
        self.driver = Getbrowser.Chrome()
    
    def testPagination(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','Pagination.html')
        driver.get(URL)
    
        pages = driver.find_element_by_class_name('yem').find_elements_by_tag_name('option') #use elements when its owns same attitubes

        print("total page is : " + str(len(driver.find_element_by_id('pageE1m_a74e_ce2c').find_elements_by_tag_name('option'))))
        for page in pages:
            #page.click()
            if page.get_attribute('value') == '6':
                page.click()
            time.sleep(2)    

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()
