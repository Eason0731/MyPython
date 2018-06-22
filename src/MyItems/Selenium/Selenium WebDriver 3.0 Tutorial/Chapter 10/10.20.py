import os
import unittest
import Browser
import time

class DoubleClick(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testDoubleClick(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.20.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        InputBox = driver.find_element_by_id('inputbox')

        from selenium.webdriver import ActionChains #导入支持双击的模块
        Action_Chains = ActionChains(driver)
        Action_Chains.double_click(InputBox).perform() #double_click()实现双击, .perform是执行
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
