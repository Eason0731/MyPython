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

class SimulateUploadFiles(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.IE()

    def testSimulateUploadFiles(self):
        driver = self.driver
        #WebSite = os.path.join('file:///',os.path.abspath('..'),'Html','11.7','upload.html')
        WebSite = "file:///D:/John's%20Code%20Project/MyPython/src/MyItems/Selenium/Selenium%20WebDriver%203.0%20Tutorial/Html/11.7/upload.html"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            wait = WebDriverWait(driver,10,0.2) #创建一个显式等待的对象
            wait.until(EC.element_to_be_clickable((By.ID,'file'))) #显式等待判断被测试页面上id为file的上传按钮是否可被点击状态
                      
        except TimeoutException as e:
            print (traceback.print_exc())
        except NoSuchElementException as e:
            print (traceback.print_exc())
        except Exception as e:
            print (traceback.print_exc())

        else:
            UploadButton = driver.find_element_by_id('file')
            UploadButton.send_keys("C:\\test.txt") #利用send_keys方法输入文件路径名
            time.sleep(2)

            SubmitButton = driver.find_element_by_id('sumbit')
            SubmitButton.click()
            time.sleep(2)
            self.assertIn('Upload file succeed!',driver.page_source,'上传失败！') #在上传成功页面判断是否上传成功,会有成功信息提示！
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
