# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait

class OperateDialog(unittest.TestCase): #11
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testOperateDialog(self): 
        driver = self.driver
        URL = 'http://www.baidu.com'
        driver.get(URL)
    
        print(driver.find_element_by_id('u1').find_element_by_name('tj_login').is_displayed())
        #driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
        driver.find_element_by_id('u1').find_element_by_name('tj_login').click() #Find the login url on the index of Baidu
        time.sleep(2)
    
        driver.find_element_by_class_name('tang-content').find_element_by_id('TANGRAM__PSP_10__userName').send_keys('Selenium') #The username box which showed on a new dialog below on 'tang-content'
        time.sleep(2)
    
        driver.find_element_by_class_name('tang-content').find_element_by_name('password').send_keys('Selenium') #The password box which showed on a new dialog below on 'tang-content'
        time.sleep(2)
    
        driver.find_element_by_class_name('tang-content').find_element_by_css_selector('input[type=submit]').click() #The login button which showed on a new dialog below on 'tang-content'
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
