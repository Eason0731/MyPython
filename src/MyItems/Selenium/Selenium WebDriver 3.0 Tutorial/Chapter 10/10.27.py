import os
import unittest
import Browser
import time

class AssertKeyWordsOnPage(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testAssertKeyWordsOnPage(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        Content = '巴西 2-0 哥斯达黎加'
        driver.find_element_by_id('sb_form_q').send_keys(Content)
        time.sleep(2)
        driver.find_element_by_id('sb_form_go').click()
        time.sleep(2)
        
        assert '巴西 2-0 哥斯达黎加' in driver.page_source,'页面源码不存在关键字' #Assert in 断言方法,判断'巴西 2-0 哥斯达黎加',是否在网页获取源码内,否则输出定义的异常返回信息
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
