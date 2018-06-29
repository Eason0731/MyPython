import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

class TestHTML5VideoPlayer(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Firefox()

    def testTestHTML5VideoPlayer(self):
        driver = self.driver
        WebSite = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_video_simple"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            self.assertIn('Your browser does not support the video tag.',driver.page_source,'未在网页中找到该关键字')
            time.sleep(2)

            VideoPlayer = driver.find_element_by_tag_name('video')
            VideoSrc = driver.execute_script("return arguments[0].currentSrc;",VideoPlayer) #使用execute_script()方法执行JavaScript语句，.currentSrc方法用户获取视频文件的网络存储地址
            self.assertEqual(VideoSrc,'http://www.w3school.com.cn/i/movie.ogg','该HTML5播放器的地址不准确')
            time.sleep(2)


            Duration = driver.execute_script("return arguments[0].duration;",VideoPlayer) #使用execute_script()方法执行JavaScript语句，.duration方法用于获取视频时间
            self.assertEqual(int(Duration),3)

            driver.execute_script("return arguments[0].play();",VideoPlayer) #使用execute_script()方法执行JavaScript语句，.play()方法可以播放视频
            time.sleep(2)

            driver.execute_script("return arguments[0].pause();",VideoPlayer) #使用execute_script()方法执行JavaScript语句，.pause()方法可以暂停视频
            time.sleep(2)

            ResultPicture = driver.save_screenshot("D:\\HTML5VideoPlayer.png") #save_screenshot方法用于截取当前屏幕
            time.sleep(2)
                    
                        
        except TimeoutException as e:
            print (traceback.print_exc())
        except NoSuchElementException as e:
            print (traceback.print_exc())
        except Exception as e:
            print (traceback.print_exc())
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
