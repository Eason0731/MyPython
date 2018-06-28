import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #导入DesiredCapabilities类

class DisableIEProtectedMode(unittest.TestCase):
    def setUp(self):
        Caps = DesiredCapabilities.INTERNETEXPLORER #创建IE浏览器的一个Caps实例对象
        Caps['ignoreProtectedModeSettings'] = True #将忽略IE保护模式的参数'ignoreProtectedModeSettings'设置为True
        
        self.driver = webdriver.Ie(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','IEDriverServer.exe')),capabilities = Caps)
        #使用相对路径找到IE浏览器驱动文件的路径，并启动,capabilities为带参数的启动

    def testDisableIEProtectedMode(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite)
        time.sleep(2)

        self.assertIn('搜狗',driver.title)
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
