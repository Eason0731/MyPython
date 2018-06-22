import os
import unittest
import Browser
import time

class OperateDropdownlistWithInput(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateDropdownlistWithInput(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.24.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.webdriver.common.keys import Keys #导入Keys模块
        Dropdownlist = driver.find_element_by_id('select')
        Dropdownlist.clear()
        
        Dropdownlist.send_keys('V',Keys.ARROW_DOWN) #输入V的同时，按下箭头键
        time.sleep(2)

        Dropdownlist.send_keys(Keys.ARROW_DOWN) #按下箭头键
        time.sleep(2)

        Dropdownlist.send_keys(Keys.ENTER) #按下回车
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
