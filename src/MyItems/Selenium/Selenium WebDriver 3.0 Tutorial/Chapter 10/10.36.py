import os
import unittest
import Browser
import time

class ImplictWait(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()
        
    def testIImplictWait(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        from selenium.common.exceptions import NoSuchElementException,TimeoutException #导入异常模块NoSuchElementException和TimeoutExeption
        import traceback #引入堆桟包
        driver.implicitly_wait(10) #使用implicitly_wait()方法，设置隐式等待时间，最长10秒
        try:
            driver.find_element_by_id('sb_form_q').send_keys('McLaren Renault')
            time.sleep(2)
            driver.find_element_by_id('sb_form_go').click()
            time.sleep(2)
        except (NoSuchElementException,TimeoutExeption) as e:
            traceback.print_exc()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
