import os
import unittest
import Browser
import time

class OperateDropdownlist(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateDropdownlist(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.21.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Dropdownlist = driver.find_element_by_name('driver')
        All_Options = driver.find_elements_by_tag_name("option")

        #去遍历下拉列表的所有内容，并输出文本值内容和属性为value的内容
        for MyDrivers in All_Options:
            print ("该车手全名为: " + MyDrivers.text)
            print ("该车手缩写为: " + MyDrivers.get_attribute('value'))
            MyDrivers.click()
            time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
