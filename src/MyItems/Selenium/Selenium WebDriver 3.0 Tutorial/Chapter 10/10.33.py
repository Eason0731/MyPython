import os
import unittest
import Browser
import time

class ClikAndHoldOnElement(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testClikAndHoldOnElement(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.33.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.webdriver import ActionChains #引入ActionChains包
        Div = driver.find_element_by_id('div1')

        for i in range(2):
            ActionChains(driver).click_and_hold(Div).perform() #使用click_and_hold()方法将模拟鼠标左键停留在元素上
            time.sleep(2)

            ActionChains(driver).release(Div).perform() #使用release()方法,去释放按下的鼠标左键
            time.sleep(2)
            
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
