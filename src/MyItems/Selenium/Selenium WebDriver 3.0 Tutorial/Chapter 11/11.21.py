import os
import unittest
import Browser
import time

class HTMLStorage(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    #@unittest.skip("skipping") #@unittest.skip("skipping")用于跳过执行该测试用例
    def testHTMLLocalStorage(self):
        driver = self.driver
        WebSite = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_webstorage_local"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        lastname = driver.execute_script("return localStorage.lastname") #使用localStorage.lastname方法去获取localStorage中的lastname值
        print (lastname)
        time.sleep(2)

        self.assertEqual('Gates',lastname) #验证Gates在lastname的值内
        time.sleep(2)

        driver.execute_script("localStorage.clear()") #使用localStorage.clear()方法去清除localStorage中所存储的内容
        time.sleep(2)

        New_lastname = driver.execute_script("return localStorage.lastname") #使用localStorage.lastname方法去获取localStorage中的lastname值
        time.sleep(2)

        self.assertEqual(None,New_lastname) #验证没有值在lastname的值内，因为被清空了
        time.sleep(2)

    def testHTMLSessionStorage(self):
        driver = self.driver
        WebSite = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_webstorage_session"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        Button = driver.find_element_by_tag_name('button')
        for i in range(5): #点击5次按钮
            Button.click()
        time.sleep(2)

        Count = driver.execute_script("return sessionStorage.clickcount") #使用sessionStorage.clickcount方法去获取单击的次数
        #print (Count)
        #print (type(Count))
        self.assertEqual('5',Count)
        
        if Count == '5': #验证按钮的点击次数
            print ("当前sessionStorage记录的次数正确")
        else:
            print ("当前sessionStorage记录的次数错误")
        
        time.sleep(2)

        driver.execute_script("sessionStorage.clear()") #使用sessionStorage.clear()方法去清除sessionStorage中所存储的内容
        New_Count = driver.execute_script("return sessionStorage.clickcount") #使用sessionStorage.clickcount方法去获取单击的次数
        #print (New_Count)
        #print (type(New_Count))
        self.assertEqual(None,New_Count)
        
        if New_Count == None: #验证按钮的点击次数
            print ("清空sessionStorage后次数正确")
        else:
            print ("清空sessionStorage后次数错误")
        
        time.sleep(2)
        
        
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
