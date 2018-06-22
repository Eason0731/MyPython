import os
import unittest
from selenium import webdriver
import time

class MaximizeBrowser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe'))) #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动

    def testMaximizeBrowser(self):
        driver = self.driver
        driver.maximize_window() #使用maximize_window()方法,最大化浏览器
        WebSite = "http://www.sogou.com"
        driver.get(WebSite) 
        time.sleep(2) #等待2秒
        assert driver.title.find('搜狗搜索引擎 - 上网从搜狗开始') >= 0 ,"assert error"  #Assert find 断言方法,判断'搜狗搜索引擎 - 上网从搜狗开始",是否在搜狗搜索主页获取的标题名内超过0次
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
