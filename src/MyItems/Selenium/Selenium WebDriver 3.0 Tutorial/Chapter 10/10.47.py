import os
import unittest
import Browser
import time

class OperateCookie(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateCookie(self):
        driver = self.driver
        WebSite = "http://www.sogou.com"
        driver.get(WebSite) 
        time.sleep(2) #等待2秒

        Cookies = driver.get_cookies() #使用get_cookies()方法获取当前页面下所有Cookies信息,并输出它们所在域，name，value，有效期和路径
        for MyCookie in Cookies:
            print ("%s -> %s -> %s -> %s -> %s" %(MyCookie['domain'],MyCookie['name'],MyCookie['value'],MyCookie['expiry'],MyCookie['path']))
            time.sleep(2)
        print ("========================================")

        Ck = driver.get_cookie('SUV') #使用get_cookie()方法获取name为SUV的Cookies信息,并输出它们所在域，name，value，有效期和路径
        print ("%s -> %s -> %s -> %s -> %s" %(Ck['domain'],Ck['name'],Ck['value'],Ck['expiry'],Ck['path']))
        time.sleep(2)
        print ("========================================")

        print (driver.delete_cookie('ABTEST')) #使用delete_cookie()方法删除name值为ABTEST的cookie记录
        time.sleep(2)
        print ("========================================")

        driver.delete_all_cookies() #使用delete_all_cookies()方法删除所有Cookies
        print (driver.get_cookies())
        time.sleep(2)
        print ("========================================")

        driver.add_cookie({'name':'EasonZhang','value':'15484999999945454'}) #使用add_cookie()方法添加Cookie,为字典格式
        time.sleep(2)
        print (driver.get_cookie('EasonZhang')) #查看刚刚添加的自定义Cookie信息
        time.sleep(2)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
