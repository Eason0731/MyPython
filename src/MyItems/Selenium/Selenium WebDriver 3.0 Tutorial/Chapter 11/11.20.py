import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

class DrawingOnHTML5Canvas(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testDrawingOnHTML5Canvas(self):
        driver = self.driver
        WebSite = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_canvas_line"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            #使用execute_script()方法执行JavaScript语句，.在HTML5的画布上进行绘图
           
            driver.execute_script("var c = document.getElementById('myCanavas');") #获取页面上的画布元素
            time.sleep(2)
            driver.execute_script("var cxt = c.getContext('2d');") #设定画布为2d
            time.sleep(2)
            driver.execute_script("cxt.fillStyle='#FF0000';") #设定填充色为红色
            time.sleep(2)               
            driver.execute_script("cxt.fillRect(0,0,150,150);") #在画布上绘制一个矩形
            time.sleep(2)
            
            ResultPicture = driver.save_screenshot("D:\\HTML5Canvas.png") #save_screenshot方法用于截取当前屏幕
            time.sleep(2)
                    
                        
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
