import os
import unittest
from selenium import webdriver
import time

class GetAndSetThePositionOfBrowserWindow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe'))) #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动

    def testGetAndSetThePositionOfBrowserWindow(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite) 
        time.sleep(2) #等待2秒

        Position = driver.get_window_position() #使用get_window_position()方法,获取当前浏览器窗口的位置
        print ("当前浏览器横坐标是:" + str(Position['x']))
        print ("当前浏览器纵坐标是:" + str(Position['y']))

        driver.set_window_position(y=200,x=400) #使用set_window_position()方法,设置浏览器窗口的位置
        time.sleep(3)
        print ("浏览器设置后的大小为:"+ str(Position))
        
        assert driver.title.find('搜狗搜索引擎 - 上网从搜狗开始') >= 0 ,"assert error"  #Assert find 断言方法,判断'搜狗搜索引擎 - 上网从搜狗开始",是否在搜狗搜索主页获取的标题名内超过0次
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
