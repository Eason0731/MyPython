import os,time,unittest,MyBrowser,HTMLTestReport
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def SearchOn360(self,driver,content):
    driver.get('https://www.so.com/?src=so.360.cn')
    time.sleep(2)
    self.assertTrue('360搜索，SO靠谱' , driver.title)
    time.sleep(2)

    content2 = ''
    driver.execute_script('arguments[0].value=arguments[1]', driver.find_element(By.XPATH,'//input[@id="input"]'),Keys.SPACE)
    time.sleep(2)
    driver.execute_script('arguments[0].value=arguments[1]', driver.find_element(By.XPATH,'//input[@id="input"]'),content)
    time.sleep(2)

    #通过XPath的定位方式来点取下拉列表候选词，方法1
    """
    Hot_Word = driver.find_element(By.XPATH,'//ul[@class="ac_menu"]//li[2]').text
    content2 = Hot_Word
    print (Hot_Word)
    time.sleep(2)

    #driver.find_element(By.XPATH,'//ul[@class="ac_menu"]//li[2]').click()
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH,'//ul[@class="ac_menu"]//li[2]'))
    time.sleep(2)
    """

    #通过XPath的定位方式来点取下拉列表候选词，方法2 (最通用和简洁)
    """
    content2 = driver.find_element(By.XPATH,'//ul[starts-with(@class,"ac_me")]//li[5]').text
    print (content2)
    time.sleep(2)

    #driver.find_element(By.XPATH,'//ul[starts-with(@class,"ac_me")]//li[5]').click()
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH,'//ul[starts-with(@class,"ac_me")]//li[5]'))
    time.sleep(2)
    """

    #通过XPath的定位方式来点取下拉列表候选词，方法3
    Hot_Word = driver.find_element(By.XPATH,'//ul[@class="ac_menu"]//li[2]')
    time.sleep(2)
    content2 = Hot_Word.text
    print (content2)
    time.sleep(2)
    
    #Hot_Word.click()
    driver.execute_script('arguments[0].click()', Hot_Word)
    #driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH,'//ul[@class="ac_menu"]//li[2]'))
    time.sleep(2)

    #通过遍历TAG_NAME为li获取下拉列表候选词框并选择指定热词
    """
    Word_List = driver.find_elements(By.TAG_NAME,'li')
    for myWord in Word_List:
        if myWord.get_attribute('li') == '0':
            content2 = myWord.text
            time.sleep(2)
            driver.execute_script('arguments[0].click()',myWord)
            time.sleep(2)
            break
    """
    if content2 + '_360搜索' in driver.page_source:
        print ('Pass on ' + content)
    else:
        print ('FAILED ON ' + content)

    time.sleep(2)
    print (driver.title)
         
    
    
class RunSearchOn360(unittest.TestCase):
    """
    def testbIE(self):
        self.driver = MyBrowser.IE()
        driver = self.driver
        SearchOn360(self,driver,'Internet Explorer')
    """
    def testcChrome(self):
        self.driver = MyBrowser.Chrome()
        driver = self.driver
        SearchOn360(self,driver,'Chrome')
    """
    def testdFirefox(self):
        self.driver = MyBrowser.Firefox()
        driver = self.driver
        SearchOn360(self,driver,'Firefox')
    
    def testaEdge(self):
        self.driver = MyBrowser.Edge()
        driver = self.driver
        SearchOn360(self,driver,'Edge')
    """
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #HTMLTestReport.HTMLTestReport('MyCase.py')
