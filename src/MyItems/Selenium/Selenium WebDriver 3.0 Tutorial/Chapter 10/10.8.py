import os
import unittest
import Browser
import time

class GetPageSource(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetPageSource(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        PageSource = driver.page_source #driver.page_source方法可以获取当前页面HTML的源码
        self.assertIn('微软 Bing 搜索 - 国内版' , PageSource) #assertIn断言方法,判断'微软"Bing 搜索 - 国内版",是否在网页获取的HTML源码内
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
