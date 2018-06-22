import os
import unittest
import Browser
import time

class GetElementAttribute(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetElementAttribute(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        SearchBox = driver.find_element_by_id('query')
        print (SearchBox.get_attribute('name')) #使用.get_attribute()方法去获取对应元素的属性名的值
        time.sleep(2)

        SearchBox.send_keys("Red Bull Honda") #send_keys()方法用于在文本框内输入指定的值
        print (SearchBox.get_attribute('value')) #使用.get_attribute()方法去获取对应元素的属性名的值
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
