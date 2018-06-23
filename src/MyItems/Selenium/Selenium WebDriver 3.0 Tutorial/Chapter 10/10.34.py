import os
import unittest
import Browser
import time

class RoverOnElement(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testRoverOnElement(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.34.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.webdriver import ActionChains #引入ActionChains包
        link1 = driver.find_element_by_id('link1')
        link2 = driver.find_element_by_partial_link_text('Again')
        p = driver.find_element_by_xpath('//p')

        ActionChains(driver).move_to_element(link1).perform() #使用move_to_element()方法，将鼠标悬浮在第一个元素上
        time.sleep(2)

        ActionChains(driver).move_to_element(p).perform() #使用move_to_element()方法，将鼠标从第一个元素上悬浮到p元素上
        time.sleep(2)
            
        ActionChains(driver).move_to_element(link2).perform() #使用move_to_element()方法，将鼠标悬浮在第二个元素上
        time.sleep(2)

        ActionChains(driver).move_to_element(p).perform() #使用move_to_element()方法，将鼠标从第二个元素上悬浮到p元素上
        time.sleep(2)
            
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
