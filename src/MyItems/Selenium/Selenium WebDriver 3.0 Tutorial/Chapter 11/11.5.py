import os
import unittest
import Browser
import time

def addAttribute(driver,elementObj,attributeName,value): #添加元素属性的封装方法
    driver.execute_script("arguments[0].%s = arguments[1]" %attributeName,elementObj,value) #使用.execute_script方法去执行JavaScript语句,去添加一个元素的新属性

def setAttribute(driver,elementObj,attributeName,value): #设置元素属性的封装方法
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",elementObj,attributeName,value) #使用.execute_script方法去执行JavaScript语句,去设置一个元素的新属性

def getAttribute(elementObj,attributeName): #获取元素属性的封装方法
    return elementObj.get_attribute(attributeName)

def removeAttribute(driver,elementObj,attributeName): #删除元素属性的封装方法
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",elementObj,attributeName) #使用.execute_script方法去执行JavaScript语句,去删除一个元素的新属性


class UpdateValueOfElement(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testUpdateValueOfElement(self):
        driver = self.driver
        WebSite = os.path.join('file:///',os.path.abspath('..'),'Html','11.5.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        InputBox = driver.find_element_by_id('text')
        addAttribute(driver,InputBox,'name','Textbox') #添加元素新属性名为name,其value值设置为'Textbox'
        print ('添加的新属性值%s="%s"' %("name",getAttribute(InputBox,"name")))#查看刚刚新添加的name属性,所赋予的值,输出应为name='Textbox'

        setAttribute(driver,InputBox,'size',20) #将文本框的size属性从100改为20
        print ("更改后元素属性size值为:",getAttribute(InputBox,'size'))

        setAttribute(driver,InputBox,'value','This is my Textbox!') #将文本框的value属性从'txt'改为'This is my Textbox!'
        print ("更改后元素属性value值为:",getAttribute(InputBox,'value'))

        removeAttribute(driver,InputBox,'name') #将文本框的value属性删除
        print ("删除后元素属性name值为:",getAttribute(InputBox,'name'))

        time.sleep(2)
               
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
