import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #导入Options类

class BanImagesOnChrome(unittest.TestCase):
    def setUp(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        profile = {"profile.managed_default_content_settings.images":2} #利用参数"profile.managed_default_content_settings.images":2，设置图片禁止加载
        Chrome_Options.add_experimental_option("prefs",profile) #添加参数
        Chrome_Options.add_argument("--disable-extensions") #利用.add_argument方法添加参数项,"--disable-extensions"表示禁用扩展程序
        
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动

    def testBanImagesOnChrome(self):
        driver = self.driver
        WebSite = "http://www.tabao.com"
        driver.get(WebSite)
        time.sleep(10)

        self.assertIn('淘宝',driver.page_source)
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
