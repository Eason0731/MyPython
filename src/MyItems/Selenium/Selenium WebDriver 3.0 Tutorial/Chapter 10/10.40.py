import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

class IdentifyNewPopUpWindowByPageSource(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testIdentifyNewPopUpWindowByPageSource(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.39.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒
        
        WebDriverWait(driver,10,0.2).until(EC.element_to_be_clickable((By.LINK_TEXT,'Baidu Search'))).click() #WebDriverWait是设置显式等待的方法,这里设置10秒等待时间,使用element_to_be_clickable()方法判断页面为Baidu Search的链接是否可被单击，并点击
        time.sleep(2)
        
        All_Handles = driver.window_handles #使用window_handles方法，获取当前所有打开浏览器的窗口句柄
        time.sleep(2)

        print (driver.current_window_handle) #使用current_window_handle方法，输出打印当前浏览器的窗口句柄
        time.sleep(2)

        print (len(All_Handles)) #输出打印打开浏览器的个数
        time.sleep(2)

        if len(All_Handles) > 0:
            try:
                for WindowHandle in All_Handles:
                    driver.switch_to_window(WindowHandle)
                    print (driver.title)
                    if '百度' in driver.page_source:
                        WebDriverWait(driver,10,0.2).until(lambda x:x.find_element_by_id('kw')).send_keys('百度首页的窗口通过源码查询被找到了!') #WebDriverWait是设置显式等待的方法,这里设置10秒等待时间,并找到百度搜索框，输入所期望的内容
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
