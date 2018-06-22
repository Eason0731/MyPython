import os
import unittest
import Browser
import time

class VisitWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testVisitWebsite(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒
        assert '微软 Bing 搜索 - 国内版' in driver.title #Assert in 断言方法,判断'微软"Bing 搜索 - 国内版",是否在网页获取的标题名内
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
