import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #导入Options类

class DownloadFileOnChrome(unittest.TestCase):
    def setUp(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        Prefs = {"download.default_directory":"D:\\ChromeDownload"} #使用"download.default_directory"参数方法设置下载的保存路径
        Chrome_Options.add_experimental_option("prefs",Prefs) #将自定义设置添加到Chrome配置对象实例当中
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动

    def testDownloadFileOnChrome(self):
        driver = self.driver
        WebSite = "https://pypi.org/project/selenium/#files"
        driver.get(WebSite)
        time.sleep(2)

        DownloadFileLink = driver.find_element_by_partial_link_text('selenium-3.13.0.tar.gz')
        DownloadFileLink.click()
        time.sleep(40)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
