import os
import unittest
import Browser
import time

class OperateWindowHandle(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateWindowHandle(self):
        driver = self.driver
        WebSite = "http://www.baidu.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Current_Handle = driver.current_window_handle #使用current_window_handle方法,获取当前窗口句柄
        print (Current_Handle)

        driver.find_element_by_id('kw').send_keys('w3cschool')
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="1"]/h3/a').click() #单击w3cschool网页链接
        time.sleep(3)

        All_Handle = driver.window_handles #获取所有窗口句柄
        print ("++++", driver.window_handles[-1])

        for Handle in All_Handle: #循环遍历所有新打开窗口的句柄，但不包括主窗口
            if Handle != Current_Handle: 
                print (Handle) #输出待选择的窗口句柄
                time.sleep(2) 
                

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
