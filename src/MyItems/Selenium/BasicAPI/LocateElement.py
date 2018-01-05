# coding:utf-8
import unittest
import os
import time
from . import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait

class LocateElement(unittest.TestCase): #9
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testLocateElement(self): 
        driver = self.driver
        URL = 'file:///' + os.path.join(os.path.abspath('.'),'Html','checkbox.html')
        driver.get(URL)
        checkboxs = driver.find_elements_by_tag_name('input') #use find_elements to find all same tag name
        radios = driver.find_elements_by_css_selector('input[type=radio]') #use find_elements to find all same css selector,css language:input[type=radio]
    
        for mycheckbox in checkboxs: #to find all tag name is input then click it
            if mycheckbox.get_attribute('type') == 'checkbox':
                mycheckbox.click()
                time.sleep(2)

        for myradiobutton in radios:
            myradiobutton.click()
            time.sleep(2)

        print(len(checkboxs)) #Count the number of same css selector
        print(len(radios))

        checkboxs.pop(1).click() #Uncheck the last selected checkbox button, pop() is empty means select the last one
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
