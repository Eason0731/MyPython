import os
import unittest
import Browser
import time

class GetElementCSSAttribute(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetElementCSSAttribute(self):
        driver = self.driver
        WebSite = "http://www.baidu.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        SearchBox = driver.find_element_by_id('kw')
        font = SearchBox.value_of_css_property('font-family')
        print ("该元素宽度为: "+SearchBox.value_of_css_property('width')) #使用.value_of_css_property()方法去获取对应元素的CSS属性的值,这里获取宽度
        print ("该元素高度为: "+SearchBox.value_of_css_property('height')) #使用.value_of_css_property()方法去获取对应元素的CSS属性的值,这里获取高度
        print ("该元素字体为: " + font) #使用.value_of_css_property()方法去获取对应元素的CSS属性的值,这里获取字体属性
        time.sleep(2)
        
        self.assertEqual(font,'arial') #assertEqual断言方法,去判断当前网页字体是否为arial
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
