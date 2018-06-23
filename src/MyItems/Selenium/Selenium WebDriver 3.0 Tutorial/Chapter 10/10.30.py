import os
import unittest
import Browser
import time

class SimulateSingleKeys(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testSimulateSingleKeys(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        from selenium.webdriver.common.keys import Keys #引入Keys包
        SearchBox = driver.find_element_by_id('sb_form_q')

        SearchBox.send_keys(Keys.F12) #输入F12键
        time.sleep(2)

        Content = '尼日利亚 2-0 冰岛'
        SearchBox.send_keys(Content) 
        time.sleep(2)

        SearchBox.send_keys(Keys.ENTER) #输入回车键 
        time.sleep(2)

        assert '尼日利亚 2-0 冰岛' in driver.title,'在标题内找不到关键词' #利用assert in断言方法判断搜索'尼日利亚 2-0 冰岛'有没有出现在标题内,否则输出自定义异常信息
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
