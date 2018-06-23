import os
import unittest
import Browser
import time

class OperateAlert(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateAlert(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.44.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        from selenium.common.exceptions import NoAlertPresentException #引入NoAlertPresentException异常模块包
        driver.find_element_by_id('button').click()
        time.sleep(2)
        try:
            Alert = driver.switch_to_alert() #使用switch_to_alert()方法获取alert对象
            print (Alert.text)
            self.assertEqual(Alert.text,'这是一个alert的弹出框') #使用断言assertEqual方法,判断获取文字是否符合预期的内容
            time.sleep(2)
            Alert.accept() #.accept()点击alert框的确认以关闭
            time.sleep(2)
        except NoAlertPresentException as e:
            print (e)
            
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
