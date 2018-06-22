import os
import unittest
import Browser
import time

class InputContentOnTextbox(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testInputContentOnTextbox(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.18.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Content = 'Hello Python Selenium'
        TextBox = driver.find_element_by_id('text')
        TextBox.clear() #利用.clear()方法清除文本框内的内容
        time.sleep(2)
        
        TextBox.send_keys(Content) #利用.send_keys()方法输入指定内容
        time.sleep(2)

        self.assertTrue(driver.page_source,Content) #assertTrue断言方法，判断文本输入指定内容是否在网页源代码内
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
