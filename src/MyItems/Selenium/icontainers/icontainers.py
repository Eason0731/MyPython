import os,Browser,time,unittest

def Login(driver,self):
    driver.find_element_by_link_text('Login').click()
    time.sleep(3)
    driver.find_element_by_id('usr-email').send_keys('lonlon29@qq.com')
    time.sleep(3)
    driver.find_element_by_id('usr-password').send_keys('54288288840')
    time.sleep(3)
    driver.find_element_by_id('btn-login').submit()
    time.sleep(5)

    self.assertIn('lonlon29',driver.page_source)
    time.sleep(3)

def Search(driver,self):
    #Choose Origin
    Origin = driver.find_element_by_name('origin')
    Origin.clear()
    Origin.send_keys('Shanghai')
    time.sleep(5)
    
    OriginDialogBox1 = driver.find_element_by_xpath("//li[contains(text(),'Shanghai (Shanghai Shi, CHINA)')]")
    OriginDialogBox1.click()
    time.sleep(5)

    OriginDialogBox2 = driver.find_element_by_xpath("//span[contains(text(),'Ship from TOWN')]")
    OriginDialogBox2.click()
    time.sleep(5)
    
    OriginSelect =driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/div/div/div/div/ul/li[1]/form/div[1]/ul[2]/li/select/option[4]")
    OriginSelect.click()

    self.assertIn('Shanghai (CHUANSHAN) - CHINA', driver.page_source)
    time.sleep(3)

    #Choose Destination
    Destination = driver.find_element_by_name('destination')
    Destination.clear()
    Destination.send_keys('Chicago')
    time.sleep(5)

    DestinationDialogBox1 = driver.find_element_by_xpath("//li[contains(text(),'Chicago (Illinois, UNITED STATES)')]")
    DestinationDialogBox1.click()
    time.sleep(5)

    DestinationDialogBox2 = driver.find_element_by_xpath("//span[contains(text(),'Ship to TOWN')]")
    DestinationDialogBox2.click()
    time.sleep(5)

    DestinationSelect =driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/div/div/div/div/ul/li[1]/form/div[3]/ul[2]/li/select/option[11]")
    DestinationSelect.click()
    time.sleep(3)

    self.assertIn('Chicago (60610) - UNITED STATES', driver.page_source)
    time.sleep(3)

    #Choose Full containers
    Container40 = driver.find_element_by_name('container40')
    Container40.send_keys('1')
    time.sleep(5)

    Highcube = driver.find_element_by_name('highcube')
    Highcube.send_keys('1')
    time.sleep(5)

    OKBtn = driver.find_element_by_link_text('OK')
    OKBtn.click()
    time.sleep(5)

    self.assertIn('1 x DV20', driver.page_source)
    self.assertIn('1 x DV40', driver.page_source)
    self.assertIn('1 x HC40', driver.page_source)
    time.sleep(3)
    
    #Submit
    driver.find_element_by_class_name('ic_widget-button').click()
    time.sleep(10)

def Method(driver):
    time.sleep(10)
    Result = driver.find_elements_by_class_name('m_table_full-body')
    count=1
    for myRes in Result:
        print ("========================Result " + str(count)+": ============================================")
        print (myRes.get_attribute('data-json'))
        count=count+1
        time.sleep(2)
        if count > 10:
            break
    print ("============================End================================================")
     
    
class GetJson(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetJson(self):
        driver = self.driver 
        driver.get('https://www.icontainers.com/')
        time.sleep(3)
        self.assertEqual('iContainers | Online Freight Forwarder - Instant Ocean Freight Quotes',driver.title)
        time.sleep(3)
        Login(driver,self)
        Search(driver,self)
        Method(driver)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main() 
