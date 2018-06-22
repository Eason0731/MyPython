import os
import unittest
import Browser
import time

class AssertOnDropdownlist(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testAssertOnDropdownlist(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.21.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.webdriver.support.ui import Select #导入Select模块
        select_element = Select(driver.find_element_by_xpath("//select")) #用xpath方法定位下拉列表
        time.sleep(2)

        actual_options = select_element.options #获取所有选择项的页面元素对象
        time.sleep(2)

        expect_optionsList = ['Fernando Alonso','Lewis Hamilton','Jenson Button','Sebastian Vettel','Kimi Raikkonen'] #声明一个List对象，存储下拉列表中所期望出现的文字内容
        time.sleep(2)
        
        actual_optionList = list(map(lambda option:option.text,actual_options)) #使用python内置的map()函数获取页面中下拉列表展示的选项内容组成的列表对象,Python3需要在map前，加一个list，否则会报错
        time.sleep(2)
        
        self.assertListEqual(expect_optionsList,actual_optionList) #断言期望列表对象和实际列表对象是否完全一致
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
