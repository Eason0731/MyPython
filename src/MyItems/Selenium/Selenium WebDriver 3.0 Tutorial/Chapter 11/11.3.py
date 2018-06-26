import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类
from selenium.webdriver.common.keys import Keys #引入Keys包

class AjaxDivOptionByKeyWords(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testAjaxDivOptionByKeyWords_1(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            SearchBox = driver.find_element_by_id('query')
            SearchBox.click()
            time.sleep(2)

            for i in range(6): #选择Ajax浮动框中第六选项,并用Keys.DOWN模拟单击下箭头
                SearchBox.send_keys(Keys.DOWN)
                time.sleep(1)

            SearchBox.send_keys(Keys.ENTER) #并用Keys.ENTER的回车键模拟回车进行搜索
            time.sleep(2)
            self.assertIn('楼市',driver.title,'未找到规定的关键字!')
            time.sleep(2)
                      
        except TimeoutException as e:
            print (traceback.print_exc())
        except NoSuchElementException as e:
            print (traceback.print_exc())
        except Exception as e:
            print (traceback.print_exc())

    def testAjaxDivOptionByKeyWords_2(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:            
            SearchBox = driver.find_element_by_id('query')
            SearchBox.click()
            time.sleep(2)

            KeyList = driver.find_element_by_xpath('//*[@id="vl"]/div[1]/ul/li[5]') #通过该关键字所在的xpath路径直接获取并点击
            KeyList.click()
            time.sleep(2)

            self.assertEqual('多地现网约护士 - 搜狗搜索',driver.title,'未找到规定的关键字!')
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
