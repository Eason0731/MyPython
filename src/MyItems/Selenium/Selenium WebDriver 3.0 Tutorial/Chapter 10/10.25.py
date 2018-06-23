import os
import unittest
import Browser
import time

class OperateRadioButton(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateRadioButton(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.25.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        AlonsoRadio = driver.find_element_by_xpath('//input[@value="Alo"]') #利用xpath方法定位Alonso的单选框
        AlonsoRadio.click()
        time.sleep(2)

        self.assertTrue(AlonsoRadio.is_selected()) #assertTrue断言方法,来判断Alonso单选框是否被选中
        time.sleep(2)

        if AlonsoRadio.is_selected(): #.is_selected()方法判断单选框是否已经被选中
            ButtonRadio = driver.find_element_by_xpath('//input[@value="But"]')
            ButtonRadio.click()
            self.assertTrue(ButtonRadio.is_selected()) #assertTrue断言方法,来判断Button单选框是否被选中
            time.sleep(2)

        AllDriversRadio = driver.find_elements_by_xpath('//input[@name="driver"]') #利用xpath方法定位所有driver的单选框
        for MyDrivers in AllDriversRadio: #遍历循环所有单选框的内容并输出和选中
            if MyDrivers.get_attribute('value') == 'Ham':
                if not MyDrivers.is_selected():
                    MyDrivers.click()
                    self.assertEqual(MyDrivers.get_attribute('value'),'Ham') #assertEqual断言方法,当前选中的单选框的value值是否为Ham
                    time.sleep(2)
            
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
