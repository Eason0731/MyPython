# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class UploadFiles(unittest.TestCase): #17
    def setUp(self):
        self.driver = Getbrowser.IE()
    
    def testUploadFiles(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','upload_file.html')
        driver.get(URL)
    
        driver.find_element_by_name('file').send_keys(URL) #Use send_keys to upload file
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
