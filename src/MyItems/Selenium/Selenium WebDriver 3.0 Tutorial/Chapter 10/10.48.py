import os
import unittest
import Browser
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class SetPageLoadTime(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testSetPageLoadTime(self):
        driver = self.driver
        driver.set_page_load_timeout(4) #使用set_page_load_timeout()方法，设置页面加载时间为4秒
        
        try:
            startTime = time.time() # time.time()为当前时间
            WebSite = "http://mail.126.com"
            driver.get(WebSite)       
        except TimeoutException as e:
            print (e)
            driver.execute_script('window.stop()') #使用excute_script()方法执行JavaScript来停止加载,'windows.stop()'为JavaScript语言

        end = time.time() - startTime #计算执行的时间
        print (end)

        driver.switch_to.frame('x - URS - iframe') #进入框架
        time.sleep(2)

        driver.find_element_by_xpath('//input[@name="email"]').send_keys('XXXX')
        time.sleep(2)

        driver.find_element_by_xpath('//input[@name="password"]').send_keys('XXXX')
        time.sleep(2)

        driver.find_element_by_xpath('//input[@name="password"]').send_keys(Keys.RETURN)
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
