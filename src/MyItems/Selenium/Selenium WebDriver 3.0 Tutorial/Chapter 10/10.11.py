import os
import unittest
import Browser
import time

class GetElementBasicInfo(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetElementBasicInfo(self):
        driver = self.driver
        WebSite = "http://www.baidu.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        nameElement = driver.find_element_by_xpath("//a[text()='更多产品']")
        print ("该元素的标签名为: " + str(nameElement.tag_name))
        print ("该元素的大小为: " + str(nameElement.size))
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
