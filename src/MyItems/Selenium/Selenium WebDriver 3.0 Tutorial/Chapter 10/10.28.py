import os
import unittest
import Browser
import time

class CaptureScreenOnCurrentWindow(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testCaptureScreenOnCurrentWindow(self):
        driver = self.driver
        WebSite = "http://www.hupu.com"
        driver.get(WebSite) #用get方法去连接想要去到的网站
        time.sleep(5) #等待5秒
        try:
            ImageFolder = os.path.join(os.path.abspath('..'),'Images')
            CurrentTime = time.strftime("%Y%m%d%H%M%S",time.localtime())
            if not os.path.exists(ImageFolder):
                os.mkdir(ImageFolder)
            Images = driver.get_screenshot_as_file(os.path.join(ImageFolder,CurrentTime+'.png')) #利用方法get_screenshot_as_file()进行截图,并保存到指定的路径
            print (Images)

        except IOError as e:
            print (e)
            
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
