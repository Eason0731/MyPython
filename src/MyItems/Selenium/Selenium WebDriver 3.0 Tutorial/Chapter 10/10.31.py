import os
import unittest
import Browser
import time

class SimulateCombinationKeys(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testSimulateCombinationKeys(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        from selenium.webdriver import ActionChains #引入ActionChains包
        from selenium.webdriver.common.keys import Keys #引入Keys包
        SearchBox = driver.find_element_by_id('sb_form_q')

        Content = '塞尔维亚 1-2 瑞士'
        SearchBox.send_keys(Content) 
        time.sleep(2)

        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform() #模拟CTRL+A全选操作,key_down()方法是按下键盘,key_up()方法是抬起键盘
        time.sleep(2)

        ActionChains(driver).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform() #模拟CTRL+X剪切操作,key_down()方法是按下键盘,key_up()方法是抬起键盘
        time.sleep(2)

        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() #模拟CTRL+V粘贴操作,key_down()方法是按下键盘,key_up()方法是抬起键盘
        time.sleep(2)
        
        SearchBox.send_keys(Keys.ENTER) #输入回车键 
        time.sleep(2)

        assert '塞尔维亚 1-2 瑞士' in driver.title,'在标题内找不到关键词' #利用assert in断言方法判断搜索'塞尔维亚 1-2 瑞士'有没有出现在标题内,否则输出自定义异常信息
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
