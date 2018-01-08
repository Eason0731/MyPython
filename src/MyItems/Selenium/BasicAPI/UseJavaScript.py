# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class UseJavaScript(unittest.TestCase): #15
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testUseJavaScript(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','js.html')
        driver.get(URL)
        time.sleep(2)

        driver.execute_script('$("#tooltip").fadeOut();') #driver.execute_script() can execute the javascript language.  fadeOut() can hide selected element. Here is "#tooltip"
        time.sleep(3)

        Button = driver.find_element_by_class_name('btn')
        #driver.execute_script('$(arguments[0]).fadeOut()',Button) #execute_script(script, *args). Note:As fadeOut() is method of Jquery,so that it should follow the grammar of Jquery. Like '$(arguments[0])'
        driver.execute_script('arguments[0].click()',Button) # As '.click()' is a method of javascript that no need to add $ before arguments
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()
