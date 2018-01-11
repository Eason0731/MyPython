# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class AlertConfirmPromptDialog(unittest.TestCase): #14

    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testAlertDialog(self): #Should start with the word "test", or it will not run the case
        driver = self.driver
        URL =  'file:///' + os.path.join(os.path.abspath('.'),'Html','Alert.html')
        driver.get(URL)

        driver.find_element_by_name('button').click()
        Alert = driver.switch_to_alert() #switch_to_alert() to get the current Alert dialog here.
        time.sleep(2)

        print(Alert.text) # .text can get the text
        Alert.accept() # .accept to click accept
        time.sleep(2)

    def testConfirmDialog(self):
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','Confirm.html')
        driver.get(URL)

        driver.find_element_by_css_selector('input[type=button]').click()
        Confirm = driver.switch_to_alert()
        time.sleep(2)

        print(Confirm.text) # .text can get the text     
        Confirm.dismiss() # .dismiss() to click cancel
        time.sleep(2)
        
        
    def testPromptDialog(self):
        self.driver = Getbrowser.IE()
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','Prompt.html')
        driver.get(URL)

        driver.find_element_by_id('button').click()
        Prompt = driver.switch_to_alert()
        time.sleep(2)

        Content = 'Hello Selenium'
        print(Prompt.text) # .text can get the text
        Prompt.send_keys(Content) #Can input word on prompt dialog use send_keys
        time.sleep(2)
        Prompt.accept() 
        time.sleep(2)
    
    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()
    
