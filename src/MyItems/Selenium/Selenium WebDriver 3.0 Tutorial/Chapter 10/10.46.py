import os
import unittest
import Browser
import time

class OperatePrompt(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperatePrompt(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.46.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.common.exceptions import NoAlertPresentException #引入NoAlertPresentException异常模块包
        driver.find_element_by_id('button').click()
        time.sleep(2)
        try:
            Prompt = driver.switch_to_alert() #使用switch_to_alert()方法获取alert对象
            print (Prompt.text)
            self.assertEqual(Prompt.text,'这是一个prompt的弹出框') #使用断言assertEqual方法,判断获取文字是否符合预期的内容
            time.sleep(2)
            Prompt.send_keys('Fernando Alonso') #在Prompt框内输入文字
            time.sleep(2)
            Prompt.dismiss() #.dismiss()点击Prompt框的取消以关闭
            #Prompt.accept() #.accept()点击Prompt框的确认以关闭
            time.sleep(2)
        except NoAlertPresentException as e:
            print (e)
            
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
