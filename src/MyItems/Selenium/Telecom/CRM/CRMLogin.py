# coding:utf-8
import os
import time
import unittest
from selenium import webdriver 
import Getbrowser

class CRMLogin(unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.IE()
    
    def testCRMLogin(self):
        CRM = 'http://10.7.68.22/ecommunications_chs/start.swe'
        Content = 'SHENJ'
        driver = self.driver
        driver.get(CRM)
        time.sleep(2)
        if '服务器正忙或出错' in driver.page_source:
            print("CRM is maintaining or busy, please try later")
        else:
            self.assertIn('上海电信客户关系管理系统',driver.page_source)
            
            UserName = driver.find_element_by_name('SWEUserName')
            Password = driver.find_element_by_name('SWEPassword')
            LoginButton = driver.find_element_by_id('s_swepi_22')
        
            UserName.send_keys(Content)
            time.sleep(2)
            Password.clear()
            time.sleep(2)
            Password.send_keys(Content)
            time.sleep(2)
            LoginButton.click()
            time.sleep(10)

            self.assertIn('UAT22',driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    
    
