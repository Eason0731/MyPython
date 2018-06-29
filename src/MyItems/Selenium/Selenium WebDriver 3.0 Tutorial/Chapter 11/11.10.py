import os
import unittest
from selenium import webdriver
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

class SetIndexByFirefoxProfile(unittest.TestCase):
    def setUp(self):
        ProPath = os.path.join(os.environ['APPDATA'],'Mozilla','Firefox','Profiles','6kqyhs92.WebDriver') #创建存储自定义配置文件的路径变量(每台机器都不一样)
        ProFile = webdriver.firefox.firefox_profile.FirefoxProfile(ProPath) #加载自定义的配置文件到FirefoxProfile的实例中
        ProFile.set_preference("browser.startup.homepage","http://cn.bing.com") #利用.set_preference()设置参数,"browser.startup.homepage"的参数是用于设置浏览器的主页
        ProFile.set_preference("browser.startup.page",1) #"browser.startup.page"参数用于设置开始页面不为空白页,0为空白页,这里设置1
        self.driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe',firefox_profile = ProFile) #在'C:\Program Files\Mozilla Firefox'启动Firefox浏览器,firefox_profile为带配置文件参数启动

    def testSetIndexByFirefoxProfile(self):
        driver = self.driver
        time.sleep(2) #等待2秒

        try:
            Content = '德国2-1瑞典'
            JS_SearchBox = "document.getElementById('sb_form_q').value='"+Content+"';"  #这是JavaScript语句：在搜索文本框内输入文字'德国2-1瑞典'，注意在JS语句中变量赋值格式如下：value='"+Content+"'，需多加一对单引号，否则会出错！
            JS_SearchButton = "document.getElementById('sb_form_go').click()" ##这是JavaScript语句：单击搜索按钮'

            driver.execute_script(JS_SearchBox) #使用execute_script()方法执行JavaScript语句，模拟输入文本框内容
            time.sleep(2)

            driver.execute_script(JS_SearchButton) #使用execute_script()方法执行JavaScript语句，模拟点击按钮
            time.sleep(2)

            self.assertEqual(Content+' - 国内版 Bing',driver.title,'该关键词未找到') #assertEqual断言方法，判断'德国2-1瑞典 - 国内版 Bing'有没有出现在当前网页获取的标题内，否则输出自定义的异常信息
                 
                        
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
