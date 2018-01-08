# coding:utf-8
import os
import time
import unittest
import Getbrowser

class Login_WOP_With_111_Account(unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.IE()

    def testLogin_WOP_With_111_Account(self):
        driver = self.driver
        WOP = 'http://10.145.206.52:8001/wop/'
        driver.get(WOP)
        time.sleep(2)
        self.assertIn("IBP施工管理系统",driver.title)
        #Login first account
        Username = driver.find_element_by_name('adminId')
        Password = driver.find_element_by_name('adminPwd')
        LoginButton = driver.find_element_by_id('but')

        Username.clear()
        Username.send_keys('123')
        time.sleep(2)
        
        Password.clear()
        Password.send_keys('abc')
        time.sleep(2)
        
        LoginButton.click()
        time.sleep(5)

        self.assertIn("上海电信施工管理平台",driver.title)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
