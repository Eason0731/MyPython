import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #导入Options类

class DisableExtensionAndMaximizeWindow(unittest.TestCase):
    def setUp(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        Chrome_Options.add_argument("--disable-extensions") #利用.add_argument方法添加参数项,"--disable-extensions"表示禁用扩展程序
        
        Chrome_Options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"]) #利用.add_experimental_option方法设置参数项,添加屏蔽"ignore - certificate - errors"的信息
        Chrome_Options.add_argument("--start-maximized") #利用.add_argument方法添加参数项,"--start-maximized"表示最大化浏览器
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动

    def testDisableExtensionAndMaximizeWindow(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2)

        driver.find_element_by_id('sb_form_q').send_keys('冰岛大狙西古德森')
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
