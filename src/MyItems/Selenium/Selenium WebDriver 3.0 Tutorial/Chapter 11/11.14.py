import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

def HighLightElement(driver,element):
        driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"background:blue;border:2px solid red;")
        #利用JavaScript语句的.setAttribute('style')方法将传进来的元素,设置背景为蓝色,边框为2px的红色

class HighLightElementWhenUsing(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testHighLightElementWhenUsing(self):
        driver = self.driver
        WebSite = "http://cn.bing.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            Content = '阿根廷绝境出线!'
            SearchBox = driver.find_element_by_id('sb_form_q')
            SearchBox.send_keys(Content)
            time.sleep(2)
            HighLightElement(driver,SearchBox)
            time.sleep(2)

            SearchButton = driver.find_element_by_id('sb_form_go')
            HighLightElement(driver,SearchButton)
            time.sleep(2)
            SearchButton.click()
            time.sleep(2)
            
            self.assertEqual(Content +' - 国内版 Bing',driver.title,'未在标题内找到关键词')
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
