# coding:utf-8
import os
import time
from . import Getbrowser
import unittest

class Search_CRM_Orders_On_P7(unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.Chrome()

    def testSearch_CRM_Orders_On_P7(self):
        #Login
        driver = self.driver
        P7URL = 'http://10.145.206.49:5001/OrderManagement/Login.jsp'
        driver.get(P7URL)
        time.sleep(3)
        self.assertIn('登录 Order and Service Management 6', driver.title)
        Username = driver.find_element_by_name('j_username')
        Password = driver.find_element_by_name('j_password')
        LoginBtn = driver.find_element_by_class_name('LoginText')

        Username.send_keys('oms-automation')
        time.sleep(2)
        Password.send_keys('passw0rd')
        time.sleep(2)
        LoginBtn.click()
        time.sleep(3)

        self.assertIn('关于 Order and Service Management 6',driver.title)
        #Login

        #Search
        QueryBtn = driver.find_element_by_name('query_')
        QueryBtn.click()
        time.sleep(3)

        """
        SearchList = driver.find_elements_by_id('currentQuery')
        for mySearch in SearchList:
            if mySearch.get_attribute('value') == 'CRM_ORDER_NUMBER':
                mySearch.click()
        """
        driver.find_element_by_id('currentQuery').click()
        time.sleep(3)
        driver.find_element_by_xpath("//option[@value='CRM_ORDER_NUMBER']").click()
        time.sleep(3)

        InputText = driver.find_element_by_name('/]reference_number_0')
        InputText.clear()
        time.sleep(2)
        CRMOrder = input("Please input CRM Order number:")
        InputText.send_keys(CRMOrder)
        time.sleep(3)

        SearchBtn = driver.find_element_by_name('Submit')
        SearchBtn.click()
        time.sleep(3)

        if CRMOrder in driver.page_source:
            print(CRMOrder + "has been set to P7 successfully!")
        else:
            print(CRMOrder + "has NOT been set to P7!")
        #Search
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
