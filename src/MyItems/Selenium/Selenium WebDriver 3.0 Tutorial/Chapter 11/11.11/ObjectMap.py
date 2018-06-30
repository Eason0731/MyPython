from selenium.webdriver.support.ui import WebDriverWait #导入显式等待包
import configparser #导入configparser包,python3中是全小写
import os
import time

class ObjectMap(object):
    def __init__(self): #获取存放页面元素定位表达方式及定位表达式的配置文件所在的绝对路径
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__)) + '\\UIObjectMap.ini'
        print((self.uiObjMapPath))

    def getElementObject(self,driver,webSiteName,elementName):
        try:
            cf = configparser.ConfigParser() #创建一个读取配置文件的实例
            cf.read(self.uiObjMapPath) #将配置文件内容加载到内存
            locators = cf.get(webSiteName,elementName).split(">") #根据section和option获取配置文件中页面元素的定位方式及定位表达式组成的字符串,并用">"分隔
            locatorMethod = locators[0] #获取定位方式
            locatorExpression = locators[1] #获取定位表达式
            print((locatorMethod,locatorExpression))
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element(locatorMethod,locatorExpression)) #通过显式等待获取页面元素
            time.sleep(2)
        
        except Exception as e:
            print (e)
        else:
            return element #当页面元素被找到时,将该页面元素对象返回给调用者
