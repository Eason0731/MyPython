import os
import unittest
import Browser
import time

class HandleIFrame(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testHandleIFrame(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.43','frameset.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        driver.switch_to.frame(0)
        assert 'This is Left side Frame' in driver.page_source

        driver.switch_to.frame(driver.find_element_by_id('showIframe')) #进入iframe框架内
        self.assertIn('This is iframe page',driver.page_source)

        driver.switch_to.default_content()
        assert 'frameset page' == driver.title
        
        driver.switch_to.frame(1)
        assert 'This is Middle side Frame' in driver.page_source
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
