import os
import unittest
import Browser
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

class OperateRichTextBox(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testOperateRichTextBox(self):
        driver = self.driver
        WebSite = "https://mail.sohu.com"
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        try:
            UserName = driver.find_element_by_xpath('//input[@placeholder="请输入您的邮箱"]') #找到用户名输入框，输入用户名
            UserName.clear()
            UserName.send_keys('baron0037@sohu.com')
            time.sleep(2)

            PassWord = driver.find_element_by_xpath('//input[@placeholder="请输入您的密码"]') #找到密码输入框,输入密码
            PassWord.clear()
            PassWord.send_keys('54288288840lon')
            time.sleep(2)

            LoginButton = driver.find_element_by_xpath('//input[@value="登 录"]') #找到登录按钮并点击
            LoginButton.click()
            time.sleep(2)

            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//li[text()="写邮件"]'))) #显式等待,确定页面是否成功登录并 跳转至登录成功的首页
            driver.find_element_by_xpath('//li[text()="写邮件"]').click()
            time.sleep(5)

            Receiver = driver.find_element_by_xpath('//div[@arr="mail.to_render"]//input') #找到收件人的输入框并输入
            Receiver.send_keys('lonlon29@qq.com;')
            time.sleep(5)

            Subject = driver.find_element_by_xpath('//input[@ng-model="mail.subject"]') #找到主题的框并输入
            Subject.send_keys('来自Selenium的测试邮件主题')
            time.sleep(5)

            MailFrame = driver.find_element_by_xpath('//iframe[contains(@id,"ueditor_0")]') #找到邮件富文本框,并进入
            driver.switch_to.frame(MailFrame)
            time.sleep(5)

            EditBox = driver.find_element_by_xpath('/html/body') #在邮件正文区域输入内容
            EditBox.send_keys('当你写下这副测试邮件的时候,就代表你的Selenium水平已经中级稳定,请继续朝向更高级的级别迈进吧,加油！----Sent By Python Selenium Scripts')
            time.sleep(5)

            driver.switch_to.default_content() #从富文本框切换出,回到默认页面
            SendButton = driver.find_element_by_xpath('//span[.="发送"]') #找到发送按钮,点击发送
            SendButton.click()
            time.sleep(5)

            self.assertIn('发送成功',driver.page_source)
            time.sleep(3)

            print ('邮件发送成功,恭喜！')

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
