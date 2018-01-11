# coding:utf-8
import unittest
import os
import time
import Getbrowser
import sys
from selenium.webdriver.support.ui import WebDriverWait #Need to import package WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #Need to import package ActionChains

class HandleCookie(unittest.TestCase): #20
    def setUp(self):
        self.driver = Getbrowser.Chrome()
        
    def testHandleCookie(self):
        driver = self.driver
        URL = 'http://www.youdao.com'
        driver.get(URL)

        driver.add_cookie({'name':'name_aaaaaa', 'value':'value_bbbb'}) #add_cookie() to add some infos on cookies. Add cookie should before then get all it will be overwrited
        cookies = driver.get_cookies() #get_cookies() to get cookies from current page
        for cookie in cookies:
            print("%s -> %s" % (cookie['name'],cookie['value'])) #To get all 'name' and 'value' cookies on current page
        print("==================================================")    
        print(cookies)

        driver.delete_cookie('CookieName') #Delete the cookie named CookieName
        driver.delete_all_cookies() # Can delete all cookies
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
   unittest.main()
