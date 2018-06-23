import os
import unittest
import Browser
import time

from selenium.webdriver import ActionChains #引入ActionChains包
import win32clipboard as w
import win32con
import win32api

class SimulateRightClick(unittest.TestCase):  
    def setUp(self):
        self.driver = Browser.Chrome()

    def testSimulateRightClick(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        from selenium.webdriver.common.keys import Keys #引入Keys包
        SearchBox = driver.find_element_by_id('sb_form_q')
        SearchBox.click()
        time.sleep(2)

        ActionChains(driver).context_click(SearchBox).perform() #使用context_click()方法,模拟右键操作
        time.sleep(2)
        
        setText('Hello Selenium') #将值设置到剪贴板中,相当于执行了复制的操作
        
        ActionChains(driver).send_keys(str(getText())).perform() #发送一个粘贴指令，字符P代替粘贴操作
        time.sleep(2)

        driver.find_element_by_id('sb_form_go').click()
        time.sleep(2)

        assert 'Hello Selenium' in driver.title,'在标题内找不到关键词' #利用assert in断言方法判断搜索'Hello Selenium'有没有出现在标题内,否则输出自定义异常信息
            
    def tearDown(self):
        self.driver.quit()

def getText():#读取剪切板    
    w.OpenClipboard()    
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)    
    w.CloseClipboard()    
    return d  

def setText(aString):#写入剪切板    
    w.OpenClipboard()    
    w.EmptyClipboard()    
    w.SetClipboardText(aString) #Python3中需要用SetClipboardText，不能用SetClipboardData了
    w.CloseClipboard() 

if __name__ == '__main__':
    unittest.main()
