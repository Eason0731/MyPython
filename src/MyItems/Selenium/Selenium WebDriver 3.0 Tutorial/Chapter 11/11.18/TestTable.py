import os
import unittest
from selenium import webdriver
import time
from Table import * #导入Table封装内容

class TestTable(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')))
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动

    def testTable(self):
        driver = self.driver
        WebSite = os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,'Html','11.18.html')
        driver.get(WebSite)
        time.sleep(2)

        WebTable = driver.find_element_by_tag_name('table') #获取测试页面中的表哥元素,存储在WebTable变量中
        table = Table(WebTable) #使用table变量对Table类进行实例化
        print ("表格中有"+ str(table.getRowCount()) +"行")
        print ("表格中有"+ str(table.getColumnCount())+"列")

        Cell = table.getCell(1,2) #获取表格中第一行第二列的单元格对象
        self.assertAlmostEqual('第一行第二列',Cell.text) #验证第一行第二列的单元格的文字是否一致
        
        CellInput = table.getWebElementInCell(3,3,'tag name','input') #获取第三行第三列中单元格的输入框对象
        CellInput.send_keys('这里的确是第三行第三列！') #在该输入框内输入指定内容

        time.sleep(3)
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
