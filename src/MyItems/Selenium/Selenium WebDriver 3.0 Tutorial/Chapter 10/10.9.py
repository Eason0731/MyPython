import os
import unittest
import Browser
import time

class GetCurrentURL(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetCurrentURL(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        CurrentURL = driver.current_url #driver.current_url方法可以获取当前网页的URL地址
        self.assertEqual(CurrentURL,"https://cn.bing.com/",'输出的URL地址非预期') #assertEqual断言方法,判断"http://cn.bing.com"是否与获取的当前页面上的URL地址是否一致
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
