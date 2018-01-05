# coding:utf-8
import os
from selenium import webdriver
import time
import unittest
import Getbrowser

class P6Login(unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.IE()

    def testP6Login(self):
        driver = self.driver
        P6 = 'http://10.7.3.94:5001/oms/'

        driver.get(P6)
        time.sleep(2)
        self.assertIn('Provisioning 6',driver.title)

        driver.find_element_by_link_text('登录 Provisioning 6').click()
        time.sleep(2)

        Username = driver.find_element_by_name('j_username')
        Password = driver.find_element_by_name('j_password')
        LoginButton = driver.find_element_by_name('submit')

        Username.clear()
        Username.send_keys('omsadmin')
        time.sleep(2)

        Password.clear()
        Password.send_keys('forxmlapi')
        time.sleep(2)

        LoginButton.click()
        time.sleep(3)

        UserID = driver.find_element_by_class_name('userID').text
        self.assertIn('omsadmin',UserID)
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
