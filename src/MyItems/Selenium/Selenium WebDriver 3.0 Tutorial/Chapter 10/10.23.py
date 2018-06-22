import os
import unittest
import Browser
import time

class OperateMultiDropdownlist(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateMultiDropdownlist(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.23.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.webdriver.support.ui import Select #导入Select模块
        Dropdownlist = Select(driver.find_element_by_xpath("//select")) #用xpath方法定位多选下拉列表
        time.sleep(2)

        Dropdownlist.select_by_index(0) #使用select_by_index()方法，通过序号选择第一个元素
        time.sleep(2)

        Dropdownlist.select_by_visible_text('Jenson Button') #使用select_by_visible_text()方法，通过选项的文本选择"Jenson Button"
        time.sleep(2)

        Dropdownlist.select_by_value('Ham') #使用select_by_value()方法，通过选项的value值'Ham'，选择"Lewis Hamilton"
        time.sleep(2)

        for MyDriver in Dropdownlist.all_selected_options: #遍历循环,利用all_selected_options方法,打印所有已经被选中的选项
            print (MyDriver.text)
            time.sleep(2)

        Dropdownlist.deselect_all() #使用deselect_all()方法，取消选择所有已选中的内容
        time.sleep(2)

        Dropdownlist.select_by_index(1) #随意选择三个选项
        Dropdownlist.select_by_visible_text('Sebastian Vettel')
        Dropdownlist.select_by_value('Rai')
        time.sleep(2)

        Dropdownlist.deselect_by_index(1) #使用deselect_by_index()方法，通过序号取消选择第二个元素
        Dropdownlist.deselect_by_visible_text('Sebastian Vettel') #使用deselect_by_visible_text()方法，通过选项的文本取消选择"Sebastian Vettel"
        Dropdownlist.deselect_by_value('Rai') #使用deselect_by_value()方法，通过选项的value值'Rai'，取消选择"Kimi Raikkonen"
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
