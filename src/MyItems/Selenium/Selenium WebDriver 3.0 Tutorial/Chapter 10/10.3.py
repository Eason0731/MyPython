import os
import unittest
import Browser
import time

class RefreshPage(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testRefreshPage(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite) 
        time.sleep(2) #等待2秒
        
        driver.refresh() #使用refresh()方法,刷新当前页面
        assert driver.title.find('搜狗搜索引擎 - 上网从搜狗开始') >= 0 ,"assert error"  #Assert find 断言方法,判断'搜狗搜索引擎 - 上网从搜狗开始",是否在搜狗搜索主页获取的标题名内超过0次
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
