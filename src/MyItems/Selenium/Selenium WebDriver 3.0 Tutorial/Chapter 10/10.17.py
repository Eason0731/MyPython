import os
import unittest
import Browser
import time

class ClearContentOnTextbox(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testClearContentOnTextbox(self):
        driver = self.driver
        WebSite = "http://www.baidu.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        SearchBox = driver.find_element_by_id('kw')
        SearchBox.send_keys('McLaren-Renault') #使用send_keys()方法在文本框内输入内容
        time.sleep(2)

        SearchBox.clear() #使用clear()方法在文本框内清除所有内容
        time.sleep(2)
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
