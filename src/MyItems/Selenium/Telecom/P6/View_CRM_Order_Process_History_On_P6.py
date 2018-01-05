# -*- coding: cp936 -*-
import os
from selenium import webdriver
import time
import unittest
import Getbrowser

class View_CRM_Order_Process_History_On_P6 (unittest.TestCase):
    def setUp(self):
        self.driver = Getbrowser.IE()

    def testView_CRM_Order_Process_History_On_P6(self):
        #Login Part
        driver = self.driver
        P6 = 'http://10.7.3.94:5001/oms/'

        driver.get(P6)
        time.sleep(2)
        self.assertIn('Provisioning 6',driver.title)

        driver.find_element_by_link_text('登录 Provisioning 6').click()
        time.sleep(2)

        Username = driver.find_element_by_name('j_username')
        Password = driver.find_element_by_name('j_password')
        LoginButton = driver.find_element_by_name('submit')

        Username.clear()
        Username.send_keys('omsadmin')
        time.sleep(2)

        Password.clear()
        Password.send_keys('forxmlapi')
        time.sleep(2)

        LoginButton.click()
        time.sleep(3)

        UserID = driver.find_element_by_class_name('userID').text
        self.assertIn('omsadmin',UserID)
        time.sleep(2)
        #Login Part
        #Search Part
        #Use list to select elements on dropdownlist
        '''
        driver.find_element_by_id('queryFormCurrentQuerySelect').click()
        DDLists = driver.find_elements_by_tag_name('option')
        for myList in DDLists:
            if myList.get_attribute('value') == 'P6 Order':
                myList.click()
        '''
        #Use xpath to select elements on dropdownlist
        '''
        driver.find_element_by_xpath('//*[@id="queryFormCurrentQuerySelect"]/option[6]').click() #P6 Order Dropdownlist
        time.sleep(2)
        '''
        #Use twice click to select elements on dropdownlist
        driver.find_element_by_id('queryFormCurrentQuerySelect').click()
        time.sleep(2)
        driver.find_element_by_xpath("//option[@value='CRM Order']").click() #P6 Order Dropdownlist
        time.sleep(2)

        #Click search button
        SearchButton = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/form/span/table/tbody/tr/td/table/tbody/tr/td[2]/input') #Searchbutton
        SearchButton.click()
        time.sleep(2)

        #Input P6 Order number
        SearchBox = driver.find_element_by_name(']reference_number_0')
        SearchBox.clear()
        CRMID = input("Please input CRM order number: ")
        SearchBox.send_keys(CRMID)
        time.sleep(2)

        #Click submit button
        SubmitButton = driver.find_element_by_name('Submit')
        SubmitButton.click()
        time.sleep(2)

        #Check P6 System in error or not
        if 'OMS Error' in driver.page_source:
            print("P6 system is in a error status now, please try again later!")
        else:
            #Check the CRMID on page or not
            if not CRMID in driver.page_source:
                print("CRM Order number : " + CRMID + " didn't been sent to P6")
            else:
                print("CRM Order number : " + CRMID + " has been sent to P6 successfully")
        #Search Part
                #View more details part
                #Choose processHistory radio button
                RadioButtons = driver.find_elements_by_css_selector('input[type=radio]')
                for myradio in RadioButtons:
                    if myradio.get_attribute('value') == 'processHistory':
                        myradio.click()
                        time.sleep(2)

                #Click details button on the left
                if '开始执行' in driver.page_source:
                    DetailsButton = driver.find_element_by_xpath('//*[@id="accepted"]/input')
                elif '已完成' in driver.page_source:
                    DetailsButton = driver.find_element_by_xpath('//*[@id="completed"]/input')
                DetailsButton.click()
                time.sleep(2)

                #Click detail infos button on the page
                driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[3]/td/form/table/tbody/tr/td/input[2]').click()
                time.sleep(3)
        
                #Check the CRMID on detail page or not
                self.assertIn('详细信息表',driver.page_source)
                self.assertIn(CRMID,driver.page_source) 
                time.sleep(2)
        
                #View more details part
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
