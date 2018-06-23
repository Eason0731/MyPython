import os
import unittest
import Browser
import time

class DragPageElement(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testDragPageElement(self):
        driver = self.driver
        WebSite = "http://jqueryui.com/resources/demos/draggable/scroll.html"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(2) #等待2秒

        initPosition = driver.find_element_by_id('draggable')
        TargetPosition = driver.find_element_by_id('draggable2')
        dragElement = driver.find_element_by_id('draggable3')

        from selenium.webdriver import ActionChains #引入ActionChains包
        ActionChains(driver).drag_and_drop(initPosition,TargetPosition).perform() #利用drag_and_drop方法将第一个元素拖拽至第二个元素
        time.sleep(2)

        for n in range(5):
            ActionChains(driver).drag_and_drop_by_offset(dragElement,10,10).perform() #利用drag_and_drop_by_offset方法，将第三个元素向右和下方向，拖动5次
            time.sleep(3)
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
