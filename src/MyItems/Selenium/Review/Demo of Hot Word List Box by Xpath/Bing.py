import MyBrowser,unittest,HTMLTestReport,time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def SearchOnBing(self,driver,content):
    driver.get('https://cn.bing.com')
    time.sleep(2)
    self.assertIn('bing' , driver.current_url)
    time.sleep(2)

    driver.execute_script('arguments[0].value=arguments[1]',driver.find_element(By.XPATH,'//input[starts-with(@class,"sb_form_q")]'),Keys.BACKSPACE)
    time.sleep(2)
    driver.execute_script('arguments[0].value=arguments[1]',driver.find_element(By.XPATH,'//input[contains(@name,"q")]'),content)
    time.sleep(2)

    content2 = ''

    #通过XPath的定位方式来点取下拉列表候选词，方法1
    """
    Hot_Word = driver.find_element(By.XPATH,'//ul[@class="sa_drw"]//li[3]')
    time.sleep(2)
    content2 = Hot_Word.text
    print (content2)
    time.sleep(2)
    
    Hot_Word.click()
    time.sleep(2)
    """
    
    #通过XPath的定位方式来点取下拉列表候选词，方法2 (最通用和简洁)
    content2 = driver.find_element(By.XPATH,'//ul[@class="sa_drw"]//li[5]').text
    print (content2)
    time.sleep(2)
    
    driver.find_element(By.XPATH,'//ul[@class="sa_drw"]//li[5]').click()
    #driver.execute_script('arguments[0].click()',driver.find_element(By.XPATH,'//ul[@class="sa_drw"]//li[5]')) #driver.execute_script方法定位不起作用,只能用click()方法
    time.sleep(2)
    
    try:
        if content2 + ' - 搜索' in driver.page_source:
            print ('Pass on ' + content)
    except Exception as e:
        print (e)
        print ('FAILED ON ' + content)
        
    print (driver.title)
    time.sleep(2)
    
class RunSearchOnBing(unittest.TestCase):
    def testaIE(self):
        self.driver = MyBrowser.IE()
        driver = self.driver
        SearchOnBing(self,driver,'迈凯伦')
    """
    def testcChrome(self):
        self.driver = MyBrowser.Chrome()
        driver = self.driver
        SearchOnBing(self,driver,'Google Chrome')

    def testbFirefox(self):
        self.driver = MyBrowser.Firefox()
        driver = self.driver
        SearchOnBing(self,driver,'Mozilla Firefox')

    def testdEdge(self):
        self.driver = MyBrowser.Edge()
        driver = self.driver
        SearchOnBing(self,driver,'Mircosoft Edge')  
    """
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #HTMLTestReport.HTMLTestReport('YongLi.py')
