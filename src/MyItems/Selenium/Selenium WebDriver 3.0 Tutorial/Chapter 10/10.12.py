import os
import unittest
import Browser
import time

class GetElementTextInfo(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetElementTextInfo(self):
        driver = self.driver
        WebSite = "http://www.baidu.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        MyElement = driver.find_element_by_xpath("//*[@class='mnav'][1]") #定位class名为mnav的第一个元素
        MyElement.text #.text方法用来获取当前定位元素的文本信息
        self.assertEqual (MyElement.text,'糯米') #assertEqual断言方法用来判断,获取元素的文本内容是否为糯米
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
