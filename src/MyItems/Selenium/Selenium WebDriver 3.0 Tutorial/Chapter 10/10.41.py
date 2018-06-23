import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException #导入期望场景类

class HandleFrame(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testHandleFrame(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.41','frameset.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        driver.switch_to.frame(0) #使用switch_to.frame()方法进入框架页面，索引从0开始，从左至右分别是0,1,2
        LeftFrameText = driver.find_element_by_xpath('//p') #找到左边框架的文字
        self.assertAlmostEqual(LeftFrameText.text,'This is Left side Frame') #assertAlmostEqual断言方法，去判断左侧框架内文字'This is Left side Frame'是否和预期文字一致
        driver.find_element_by_tag_name('input').click() #点击左侧框架的按钮
        time.sleep(2)

        try:
            alertWindow = WebDriverWait(driver,10).until(EC.alert_is_present()) #WebDriverWait是设置显式等待的方法，这里设置10秒等待时间,直到alert框弹出
            print (alertWindow.text)
            time.sleep(2)
            alertWindow.accept()
        except TimeoutException as e:
            print (e)
        
        driver.switch_to.default_content() #使用switch_to_default.content()方法回到默认页，不使用该方法，是无法进入其他frame框架
        driver.switch_to.frame(driver.find_elements_by_tag_name('frame')[1]) #进入中间的frame框架
        assert 'This is Middle side Frame' in driver.page_source #判断'This is Middle side Frame'是否在当前frame内
        driver.find_element_by_tag_name('input').send_keys('I am on the middle side frame!')
        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_id('rightframe')) #进入右边的frame框架
        assert 'This is Right side Frame' in driver.page_source #判断'This is Right side Frame'是否在当前frame内
        time.sleep(2)
        
        driver.switch_to.default_content()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
