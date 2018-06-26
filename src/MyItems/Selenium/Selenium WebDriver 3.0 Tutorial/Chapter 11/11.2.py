import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

class OperateScollBarOnWebPage(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateScollBarOnWebPage(self):
        driver = self.driver
        WebSite = "http://www.sina.com.cn"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            driver.execute_script("window.scrollTo(100,document.body.scrollHeight);") #使用execute_script()方法执行JavaScript语句，JS语句"window.scrollTo(100,document.body.scrollHeight)"表示将滚动条拖到最下方
            time.sleep(3)

            driver.execute_script("document.getElementsByName('SerchKey')[0].scrollIntoView(true);") #使用execute_script()方法执行JavaScript语句，JS语句".scrollIntoView(true)"表示将元素滚到屏幕中央,false表示将元素滚到屏幕底部,因为新浪首页中有两个name为'SerchKey'的元素，这里取第一个，利用[0]
            time.sleep(3)

            driver.execute_script("window.scrollBy(0,400);") #使用execute_script()方法执行JavaScript语句，JS语句".scrollBy(0,400)"表示将页面向下滚动400像素
            time.sleep(3)
                      
        except TimeoutException as e:
            print (traceback.print_exc())
        except NoSuchElementException as e:
            print (traceback.print_exc())
        except Exception as e:
            print (traceback.print_exc())
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
