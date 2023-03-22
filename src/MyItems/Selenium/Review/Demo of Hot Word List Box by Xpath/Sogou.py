import os,time,unittest,EasonBrowser,HTMLTestReport
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def SearchOnSogou(self,driver,content):
    driver.get('https://www.sogou.com')
    time.sleep(2)
    self.assertTrue('搜狗搜索引擎 - 上网从搜狗开始' , driver.title)
    time.sleep(2)

    driver.execute_script('arguments[0].value=arguments[1]', driver.find_element(By.XPATH,'//input[starts-with(@name,"que")]'),Keys.BACKSPACE)
    time.sleep(2)
    driver.execute_script('arguments[0].value=arguments[1]', driver.find_element(By.XPATH,'//input[starts-with(@name,"que")]'),content)
    time.sleep(2)

    content2 = driver.find_element(By.XPATH,'//ul[starts-with(@class,"sugli")]//li[2]').text
    time.sleep(2)
    driver.execute_script('arguments[0].click()',driver.find_element(By.XPATH,'//ul[starts-with(@class,"sugli")]//li[2]'))
    #driver.find_element(By.XPATH,'//ul[starts-with(@class,"sugli")]//li[2]').click()
    time.sleep(2)
    
    try:
        if content2 + ' - 搜狗搜索' in driver.page_source:
            print ('Pass on ' + content)
    except Exception as e:
        print (e)
        print ('FAILED ON ' + content)

    time.sleep(2)
    print (driver.title)
    time.sleep(2)
    print ('=====================================')

class RunSearchOnSogou(unittest.TestCase):
    def testaIE(self):
        self.driver = EasonBrowser.IE()
        driver = self.driver
        SearchOnSogou(self,driver,'Internet Explorer')
    
    def testbChrome(self):
        self.driver = EasonBrowser.Chrome()
        driver = self.driver
        SearchOnSogou(self,driver,'Chrome')

    def testcFirefox(self):
        self.driver = EasonBrowser.Firefox()
        driver = self.driver
        SearchOnSogou(self,driver,'Firefox')

    def testdEdge(self):
        self.driver = EasonBrowser.Edge()
        driver = self.driver
        SearchOnSogou(self,driver,'Edge')
    
    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    #unittest.main()
    HTMLTestReport.HTMLTestReport('EasonCase.py')
