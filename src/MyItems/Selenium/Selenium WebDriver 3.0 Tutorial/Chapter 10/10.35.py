import os
import unittest
import Browser
import time

class IsElementPresentOrNot(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def isElementPresent(self,by,value):
        from selenium.common.exceptions import NoSuchElementException #导入异常模块NoSuchElementException
        try:
            element = self.driver.find_element(by=by,value=value) #判断传入的参数元素是否存在打开的页面
        except NoSuchElementException as e:
            print (e)
        else:
            return True

    def testIsElementPresentOrNot(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        Result = self.isElementPresent('id','sb_form_q') #调用isElementPresent方法来判断页面是否存在
        if Result is True:
            print ("所查找的元素存在于页面上")
        else:
            print ("页面中未找到所要找的元素")
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
