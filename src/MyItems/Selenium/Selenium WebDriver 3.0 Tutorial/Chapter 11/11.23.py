import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #导入Options类

def SearchOnBing(driver,Content):
        #driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2)
        
        SearchBox = driver.find_element_by_id('sb_form_q')
        SearchBox.send_keys(Content)
        time.sleep(2)

        if 'iPad' in Content: #除了ipad打开浏览器页面和PC端一样,安卓和iPhone打开的均为移动端页面,搜索按钮的Id不同
            BtnName = 'sb_form_go'
        else:
            BtnName = 'sbBtn'
        
        SearchButton = driver.find_element_by_id(BtnName)
        SearchButton.click()
        time.sleep(2)

        assert Content + ' - 国内版 Bing' in driver.title
        time.sleep(2)
         
class EditChromeForMobileVersion(unittest.TestCase):
    def testChromeiPad(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        Chrome_Options.add_argument("--user-agent=Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/67.0.3396.99 Mobile/13B143 Safari/601.1.46") #使用.add_argument方法体检参数,设置ipad的Chrome浏览器的user agent字符串
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动
        driver = self.driver
        SearchOnBing(driver,'ChromeiPad')
        
        driver.get('chrome://version')
        self.assertIn('iPad',driver.page_source)
        time.sleep(5)
        
        driver.quit()
    
    def testChromeiPhone(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        Chrome_Options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/67.0.3396.99 Mobile/13B143 Safari/601.1.46") #使用.add_argument方法体检参数,设置iPhone的Chrome浏览器的user agent字符串
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动
        driver = self.driver
        SearchOnBing(driver,'ChromeiPhone')
        
        driver.get('chrome://version')
        self.assertIn('iPhone',driver.page_source)
        time.sleep(5)
        
        driver.quit()
    
    def testChromeAndroid402(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        Chrome_Options.add_argument("--user-agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30") #使用.add_argument方法体检参数,设置安卓4.0.2版本的Chrome浏览器的user agent字符串
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动
        driver = self.driver
        SearchOnBing(driver,'ChromeAndroid402')
        
        driver.get('chrome://version')
        self.assertIn('Android 4.0.2',driver.page_source)
        time.sleep(5)
    
        driver.quit()

    def testChromeAndroid236(self):
        Chrome_Options = Options() #创建Chrome浏览器的一个Options实例对象
        Chrome_Options.add_argument("--user-agent=Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1") #使用.add_argument方法体检参数,设置安卓2.3.6版本的Chrome浏览器的user agent字符串
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')),options = Chrome_Options)
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动
        driver = self.driver
        SearchOnBing(driver,'ChromeAndroid236')
        
        driver.get('chrome://version')
        self.assertIn('Android 2.3.6',driver.page_source)
        time.sleep(5)
    
        driver.quit()

if __name__ == '__main__':
    unittest.main()
