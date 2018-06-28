import os
import unittest
from selenium import webdriver
import time

class BanCSSFlashImagesOnFirefox(unittest.TestCase):
    def setUp(self):
        Profile = webdriver.FirefoxProfile()
        Profile.set_preference("permissions.default.stylesheet",2) #利用"permissions.default.stylesheet",2参数设置CSS禁止加载
        Profile.set_preference("permissions.default.image",2) #利用"permissions.default.image",2参数设置图片禁止加载
        Profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so",False) #利用"dom.ipc.plugins.enabled.libflashplayer.so",False参数,设置Flash禁止加载
        
        self.driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
        #在'C:\Program Files\Mozilla Firefox'启动Firefox浏览器

    def testBanCSSFlashImagesOnFirefox(self):
        driver = self.driver
        WebSite = "http://www.iqiyi.com"
        driver.get(WebSite)
        time.sleep(10)

        self.assertIn('爱奇艺',driver.page_source)
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
