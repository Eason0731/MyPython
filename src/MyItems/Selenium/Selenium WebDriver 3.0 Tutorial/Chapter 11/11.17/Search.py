import os
import unittest
from selenium import webdriver
import time,traceback
import Log #导入Log封装类的所有内容

class SearchWithLog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')))
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动,options为带参数的启动

    def testSearchWithLog(self):
        driver = self.driver
        Log.info("====================搜索=======================") #调用Log.py的info方法,来打印info消息级别的日志
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2)
        Content = '2018 Formula 1 Austrian Grand Prix'
        Log.info("访问Bing搜索主页") #调用Log.py的info方法,来打印info消息级别的日志
        searchBox = driver.find_element_by_id('sb_form_q')
        searchBox.send_keys(Content)
        time.sleep(2)
        Log.info("在输入框中输入2018 Formula 1 Austrian Grand Prix") #调用Log.py的info方法,来打印info消息级别的日志
        searchButton = driver.find_element_by_id('sb_form_go')
        searchButton.click()
        time.sleep(2)
        Log.info("点击搜索按钮") #调用Log.py的info方法,来打印info消息级别的日志
        self.assertIn(Content +' - 国内版 Bing' ,driver.page_source)
        time.sleep(2)
        Log.info("验证搜索关键字是否与网页标题内容相符") #调用Log.py的info方法,来打印info消息级别的日志
        Log.info("=============测试用例执行结束===================") #调用Log.py的info方法,来打印info消息级别的日志
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
