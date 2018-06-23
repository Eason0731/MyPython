import os
import unittest
import Browser
import time

class HandleFrameByPageSource(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testHandleFrameByPageSource(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.41','frameset.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        frameList = driver.find_elements_by_tag_name('frame')

        for myFrame in frameList:
            driver.switch_to.frame(myFrame) #遍历进入所有的frame框架
            if 'This is Middle side Frame' in driver.page_source:
                p = driver.find_element_by_xpath('//p')
                driver.find_element_by_id('text').send_keys('I am on the middle side frame now!')
                time.sleep(2)
                self.assertAlmostEqual('This is Middle side Frame',p.text) #assertAlmostEqual断言方法，判断'This is Middle side Frame'是否在当前frame内
                driver.switch_to.default_content() #使用switch_to_default.content()方法回到默认页，不使用该方法，是无法进入其他frame框架
                break
            else:
                driver.switch_to.default_content() #使用switch_to_default.content()方法回到默认页，不使用该方法，是无法进入其他frame框架
                
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
