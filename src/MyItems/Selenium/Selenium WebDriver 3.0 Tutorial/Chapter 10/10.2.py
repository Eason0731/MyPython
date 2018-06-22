import os
import unittest
import Browser
import time

class BackAndForward(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testBackAndForward(self):
        driver = self.driver
        WebSite1 = "http://cn.bing.com"
        WebSite2 = "http://www.sogou.com"
        driver.get(WebSite1) 
        time.sleep(2) 
        driver.get(WebSite2) 
        time.sleep(2) #等待2秒

        driver.back() #使用back()方法,回退至WebSite1网站
        assert '微软 Bing 搜索 - 国内版' in driver.title #Assert in 断言方法,判断'微软"Bing 搜索 - 国内版",是否在bing搜索主页获取的标题名内
        time.sleep(2)
        
        driver.forward() #使用forward()方法,前进至WebSite2网站
        assert '搜狗搜索引擎 - 上网从搜狗开始' in driver.title #Assert in 断言方法,判断'搜狗搜索引擎 - 上网从搜狗开始",是否在搜狗搜索主页获取的标题名内
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
