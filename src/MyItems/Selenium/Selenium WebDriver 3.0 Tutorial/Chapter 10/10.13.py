import os
import unittest
import Browser
import time

class IsDispalyedOrNot(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testIsDispalyedOrNot(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.13.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Div2 = driver.find_element_by_id('div2')
        print (Div2.is_displayed()) #.is_displayed()方法来判断页面元素是否可见
        time.sleep(2)

        driver.find_element_by_id('button1').click() #.click()方法是单击操作
        print (Div2.is_displayed()) #.is_displayed()方法来判断页面元素是否可见
        time.sleep(2)

        Div4 = driver.find_element_by_id('div4')
        print (Div4.is_displayed()) #.is_displayed()方法来判断页面元素是否可见
        time.sleep(2)

        driver.find_element_by_id('button2').click() #.click()方法是单击操作
        print (Div4.is_displayed()) #.is_displayed()方法来判断页面元素是否可见
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
