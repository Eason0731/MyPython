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

class OperateDatePick(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateDatePick(self):
        driver = self.driver
        WebSite = "http://jqueryui.com/resources/demos/datepicker/other-months.html"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            DatePick = driver.find_element_by_id('datepicker')
            DatePick.click()
            time.sleep(2)
            
            DatePick.send_keys('07/31/2018')
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
