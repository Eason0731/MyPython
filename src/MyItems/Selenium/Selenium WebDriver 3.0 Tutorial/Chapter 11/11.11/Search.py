import os
import unittest
from selenium import webdriver
import time,traceback
from ObjectMap import ObjectMap #导入ObjectMap包

class SearchByObjectMap(unittest.TestCase):
    def setUp(self):
        self.obj = ObjectMap()
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')))
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动

    def testSearchByObjectMap(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2)
        Content = '2018 Formula 1 Austrian Grand Prix'
        try:
            searchBox = self.obj.getElementObject(driver,'Bing','searchBox')
            searchBox.send_keys(Content)
            time.sleep(2)

            searchButton = self.obj.getElementObject(driver,'Bing','searchButton')
            searchButton.click()
            time.sleep(2)

            self.assertIn(Content +' - 国内版 Bing' ,driver.page_source)
            time.sleep(2)
            
        except Exception as e:
            print((traceback.print_exc()))

        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
