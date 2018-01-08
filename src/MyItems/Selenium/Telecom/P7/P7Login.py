# coding:utf-8
import os
import time
import Getbrowser
import unittest

class P7Login(unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.Chrome()

    def testP7Login(self):
        driver = self.driver
        P7URL = 'http://10.145.206.49:5001/OrderManagement/Login.jsp'
        driver.get(P7URL)
        time.sleep(3)
        self.assertIn('登录 Order and Service Management 6', driver.title)
        Username = driver.find_element_by_name('j_username')
        Password = driver.find_element_by_name('j_password')
        LoginBtn = driver.find_element_by_class_name('LoginText')

        Username.send_keys('oms-automation')
        time.sleep(2)
        Password.send_keys('passw0rd')
        time.sleep(2)
        LoginBtn.click()
        time.sleep(3)

        self.assertIn('关于 Order and Service Management 6',driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
