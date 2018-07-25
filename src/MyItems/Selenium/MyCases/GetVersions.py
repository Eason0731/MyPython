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
        print ("Latest Edge driver version is: " + EdgeDriverVersion.text)
        time.sleep(3)
    
    def testGetGeckoDriverVersion(self):
        driver = self.driver
        driver.get("https://github.com/mozilla/geckodriver/releases")
        time.sleep(3)

        GeckoDriverVersion = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/h1/a')
        print ("Latest Gecko driver version is: " + GeckoDriverVersion.text)
        time.sleep(3)
    
    def testGetGitVersion(self):
        driver = self.driver
        driver.get("https://git-scm.com/")
        time.sleep(3)

        GitVersion = driver.find_element_by_xpath('//*[@id="front-downloads"]/div/span[1]')
        print ("Latest Git version is: " + GitVersion.text)
        time.sleep(3)
    
    def testGetJava8Version(self):
        driver = self.driver
        driver.get("http://www.oracle.com/technetwork/java/index.html")
        time.sleep(3)

        JavaVersion = driver.find_element_by_xpath('//*[@id="hm1w1"]/div[6]/ul/li[2]/a')
        print ("Latest Java 8 version is: " + JavaVersion.text)
        time.sleep(3)
    
    def testGetPythonVersion(self):
        driver = self.driver
        driver.get("https://www.python.org/downloads/")
        time.sleep(3)

        PythonVersion = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[1]/ol/li[1]/span[1]/a')
        print (PythonVersion.text)
        time.sleep(3)
    
    def testGetSeleniumVersion(self):
        driver = self.driver
        driver.get("https://docs.seleniumhq.org/download/")
        time.sleep(3)

        SeleniumVersion = driver.find_element_by_xpath('//*[@id="mainContent"]/p[3]/a')
        print ("Latest Selenium version is: " + SeleniumVersion.text)
        time.sleep(3)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
