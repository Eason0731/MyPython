import os
import unittest
import Browser
import time

class IsEnableOrNot(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testIsEnableOrNot(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.14.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Input1 = driver.find_element_by_id('input1')
        print (Input1.is_enabled()) #.is_enabled()方法来判断页面元素是否可可操作
        time.sleep(2)

        Input2 = driver.find_element_by_id('input2')
        print (Input2.is_enabled()) #.is_enabled()方法来判断页面元素是否可可操作
        time.sleep(2)

        Input3 = driver.find_element_by_id('input3')
        print (Input3.is_enabled()) #.is_enabled()方法来判断页面元素是否可可操作
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
