import os
import unittest
import Browser
import time

class ClickButton(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testClickButton(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.19.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        self.assertTrue(driver.page_source,'文本框的默认内容') #assertTrue断言方法，判断文本框默认文字是否在网页源代码内
        Button = driver.find_element_by_id('button')
        Button.click() #使用.click()方法单击按钮
        time.sleep(2)

        self.assertTrue(driver.page_source,'改变了') #assertTrue断言方法，判断文本框默认文字是否在网页源代码内
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
