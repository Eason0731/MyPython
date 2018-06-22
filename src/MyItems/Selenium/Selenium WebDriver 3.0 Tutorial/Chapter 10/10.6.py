import os
import unittest
from selenium import webdriver
import time

class GetAndSetThePositionOfBrowserSize(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe'))) #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动

    def testGetAndSetThePositionOfBrowserSize(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite) 
        time.sleep(2) #等待2秒

        Size = driver.get_window_size() #使用get_window_size()方法,获取当前浏览器窗口的位置
        print ("当前浏览器宽度为:" + str(Size['width']))
        print ("当前浏览器高度为:" + str(Size['height']))
        time.sleep(3)
        
        driver.set_window_size(width=800,height=600) #使用set_window_size()方法,设置浏览器大小的位置为宽800,高600,windowHandle='current'为屏幕中央(此参数可有可无)
        time.sleep(3)
        print ("浏览器设置后的窗口大小为:"+ str(driver.get_window_size()))
           
        assert driver.title.find('搜狗搜索引擎 - 上网从搜狗开始') >= 0 ,"assert error"  #Assert find 断言方法,判断'搜狗搜索引擎 - 上网从搜狗开始",是否在搜狗搜索主页获取的标题名内超过0次
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
