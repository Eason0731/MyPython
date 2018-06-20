import os
import unittest
import Browser
import time

class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.IE()

    def testRunTestCase(self):
        driver = self.driver
        driver.get("http://cn.bing.com")
        time.sleep(2)
        self.assertTrue('微软',driver.page_source)
        time.sleep(2)

        Content = "McLaren-Renault"
        driver.find_element_by_id('sb_form_q').send_keys(Content)
        time.sleep(2)
        driver.find_element_by_id('sb_form_go').click()
        time.sleep(2)

        self.assertEqual(Content+' - 国内版 Bing',driver.title)
        time.sleep(2)
        print (driver.title)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
