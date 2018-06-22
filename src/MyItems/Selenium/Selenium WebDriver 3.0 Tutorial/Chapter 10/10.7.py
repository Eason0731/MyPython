import os
import unittest
import Browser
import time

class GetTitle(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetTitle(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Title = driver.title #driver.title方法可以获取当前页面的标题名
        self.assertEqual('微软 Bing 搜索 - 国内版' ,Title,'页面Title属性值错误！') #assertEqual断言方法,判断'微软"Bing 搜索 - 国内版",是否与网页获取的标题名一致
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
