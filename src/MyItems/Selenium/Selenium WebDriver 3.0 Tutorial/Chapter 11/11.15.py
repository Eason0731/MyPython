import os
import unittest
import Browser
import time
import win32api,win32con #引入Windows的win32组件

VK_CODE = {'ctrl':0x11, 't':0x54 , 'tab':0x09}

def KeyDown(keyName): #封装键盘按下的方法
	win32api.keybd_event(VK_CODE[keyName],0,0,0)

def KeyUp(keyName): #封装键盘抬起的方法
	win32api.keybd_event(VK_CODE[keyName],0,win32con.KEYEVENTF_KEYUP,0)

def SimulateKey(FirstKey,SecondKey): #封装按键的方法
	KeyDown(FirstKey)
	KeyDown(SecondKey)
	KeyUp(FirstKey)
	KeyUp(SecondKey)
        
class OpenNewTabOnBrowser(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOpenNewTabOnBrowser(self):
        driver = self.driver
        for n in range(2): #按2次CTRL+TAB,打开两个浏览器的新标签页
                SimulateKey('ctrl','t')
                time.sleep(1)
        time.sleep(2)

        SimulateKey('ctrl','tab') #按下CTRL+TAB返回最先打开的标签页
        time.sleep(2)
			
        WebSite1 = "http://cn.bing.com"
        WebSite2 = "http://www.sogou.com"
        WebSite3 = "http://so.360.cn" 
        Content = '比利时获得小组第一'

        driver.get(WebSite1)
        time.sleep(2) #等待2秒
        driver.find_element_by_id('sb_form_q').send_keys(Content)
        time.sleep(2)
        driver.find_element_by_id('sb_form_go').click()
        time.sleep(2)
        self.assertEqual(Content + ' - 国内版 Bing',driver.title)
        time.sleep(2)

        All_Handles = driver.window_handles #获取所有窗口打开的句柄
        print ("The number of Chrome opened tab is ", len(All_Handles))

        driver.switch_to.window(All_Handles[1]) #利用switch_to.window()方法切换窗口,All_Handles[1]为第二个标签页,此时切换到第二个标签页继续操作
        driver.get(WebSite2)
        time.sleep(2) #等待2秒
        driver.find_element_by_id('query').send_keys(Content)
        time.sleep(2)
        driver.find_element_by_id('stb').click()
        time.sleep(2)
        self.assertTrue(Content + ' - 搜狗搜索',driver.title)
        time.sleep(2)

        driver.switch_to.window(All_Handles[2]) #利用switch_to.window()方法切换窗口,All_Handles[2]为第三个标签页,此时切换到第三个标签页继续操作
        driver.get(WebSite3)
        time.sleep(2) #等待2秒
        driver.find_element_by_name('q').send_keys(Content)
        time.sleep(2)
        driver.find_element_by_id('search-button').click()
        time.sleep(2)
        self.assertIn(Content + '_360搜索',driver.page_source)
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
