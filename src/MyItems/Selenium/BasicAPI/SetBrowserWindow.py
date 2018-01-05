import os
from selenium import webdriver
import unittest
from . import Getbrowser
import time

class SetBrowserWindow(unittest.TestCase): #3
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        time.sleep(3)

    def testSetBrowserWindow(self):
        URL = 'http://www.baidu.com'
        driver = self.driver
        driver.set_window_size(800,600) #set_window_size can custom the window size of current browser
        time.sleep(2)
        driver.get(URL)
        print(driver.current_url)
        print(driver.title)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
