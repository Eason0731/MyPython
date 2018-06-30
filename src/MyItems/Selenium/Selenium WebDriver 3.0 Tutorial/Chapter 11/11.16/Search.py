import os
import unittest
from selenium import webdriver
import time
import traceback #引入堆栈类
import FileUtil

from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

picDir = FileUtil.createDir() #调用FileUtil封装类中的createDir方法创建目录

def takeScreenShot(driver,savePath,picName): #封装截屏方法
    picPath = os.path.join(savePath,str(picName) + ".png") #构造屏幕截图的路径和图片名,注意:在Python3中无编码影响不需要转换,在Python2中需要将存储的图片名修改为:str(picName).decode('utf-8').decode('gbk') + ".png"
    try:
        driver.get_screenshot_as_file(picPath)#使用.get_screenshot_as_file()方法,将截取的屏幕图片保存为本地文件
    except Exception as e:
        print (traceback.print_exc())

class CapturePictureWhenCaseFailed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe')))
        #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动

    def testCapturePictureWhenCaseFailed(self):
        try:
            driver = self.driver
            WebSite = "http://cn.bing.com"
            driver.get(WebSite)
            time.sleep(2)

            Content = '2018 Formula 1 Austrian Grand Prix'
            searchBox = driver.find_element_by_id('sb_form_q')
            searchBox.send_keys(Content)
            time.sleep(2)

            searchButton = driver.find_element_by_id('sb_form_go')
            searchButton.click()
            time.sleep(2)

            self.assertIn(Content +' - 国际版 Bing' ,driver.title)
            time.sleep(2)
        except AssertionError as e:
            takeScreenShot(driver,picDir,e) #执行测试用例失败后,在抛出异常模块调用截图方法以查看执行失败的图片
        except Exception as e:
            print (traceback.print_exc())
            takeScreenShot(driver,picDir,e) #执行测试用例失败后,在抛出异常模块调用截图方法以查看执行失败的图片
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
