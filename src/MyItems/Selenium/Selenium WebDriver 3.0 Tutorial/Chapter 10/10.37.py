import os
import unittest
import Browser
import time

class ExplicitWait(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testExplicitWait(self):
        driver = self.driver
        WebSite = os.path.join(os.path.abspath('..'),'Html','10.37.html')
        driver.get(WebSite)
        time.sleep(2) #等待2秒

        import traceback #引入堆栈类
        from selenium.webdriver.common.by import By #导入By类
        from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类

        try:
            wait = WebDriverWait(driver,10,0.2) #WebDriverWait是设置显式等待的方法，这里设置10秒等待时间
            wait.until(EC.title_is('10.37'))

            element = driver.find_element_by_xpath("//input[@value='Display alert box']")
            element.click()

            alert = wait.until(EC.alert_is_present()) #等待alert框出现
            print (alert.text)
            time.sleep(2)
            alert.accept() #点击确认
            time.sleep(2)

            Alo = driver.find_element_by_id('alonso')
            wait.until(EC.element_to_be_selected(Alo)) #element_to_be_selected()方法用于判断在下拉列表中的元素是否被选中
            time.sleep(2)
            print ("下拉列表的Fernando Alonso已经是被选中的状态")

            wait.until(EC.element_to_be_clickable((By.ID,'check'))) #element_to_be_clickable()方法用于判断复选框是否可被单击
            time.sleep(2)
            print ("复选框可见并且能被单击")

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
