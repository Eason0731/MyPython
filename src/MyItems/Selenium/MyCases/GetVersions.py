import os,time,unittest,Browser

class GetVersions(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.Chrome()

    def testGetChromeDriverVersion(self):
        driver = self.driver
        driver.get("https://sites.google.com/a/chromium.org/chromedriver/")
        time.sleep(3)

        ChromeDriverVersion = driver.find_element_by_xpath('//*[@id="sites-canvas-main-content"]/table/tbody/tr/td/div/h2/font/a')
        print (ChromeDriverVersion.text)
        time.sleep(3)

    def testGetEdgeDriverVersion(self):
        driver = self.driver
        driver.get("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
        time.sleep(3)

        EdgeDriverVersion = driver.find_element_by_xpath('//*[@id="downloads"]/div/div[2]/ul/li[2]/a')
        print (EdgeDriverVersion.text)
        time.sleep(3)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
