import os
import unittest
import Browser
import time

class OperateCheckboxButton(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateCheckboxButton(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.26.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        AlonsoCheckbox = driver.find_element_by_xpath('//input[@value="Alo"]') #利用xpath方法定位Alonso的复选框
        AlonsoCheckbox.click()
        time.sleep(2)

        self.assertTrue(AlonsoCheckbox.is_selected()) #assertTrue断言方法,来判断Alonso复选框是否被选中
        time.sleep(2)

        if AlonsoCheckbox.is_selected(): #.is_selected()方法判断复选框是否已经被选中
            ButtonCheckbox = driver.find_element_by_xpath('//input[@value="But"]')
            ButtonCheckbox.click()
            self.assertTrue(ButtonCheckbox.is_selected()) #assertTrue断言方法,来判断Button复选框是否被选中
            time.sleep(2)

        AllDriversCheckbox = driver.find_elements_by_xpath('//input[@name="driver"]') #利用xpath方法定位所有driver的复选框
        for MyDrivers in AllDriversCheckbox: #遍历循环所有复选框的内容并输出和选中
            if not MyDrivers.is_selected():
                MyDrivers.click()
                time.sleep(2)
            
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
