# coding:utf-8
import os
from selenium import webdriver 
import time
import sys

def IE():
    if os.name == 'nt':
        IEdriver = os.path.join(os.path.abspath('.'),'Drivers','IEDriverServer.exe') #Use relative path to get the path of IEDriverServer
        os.environ["webdriver.ie.driver"] = IEdriver # Set a system environment for ie browser then load IEDriverServer file path
        driver = webdriver.Ie(IEdriver)# Lanuch IE browser
        RunSogou(driver,sys._getframe().f_code.co_name)
    else:
        print("IE cannot be ran on non-Windows OS")
    
def Chrome():
    if os.name == 'nt':
        ChromeDriver = os.path.join(os.path.abspath('.'),'Drivers','ChromeDriver.exe')  
    elif os.name == 'posix':
        ChromeDriver = os.path.join(os.path.abspath('.'),'Drivers','ChromeDriver')
    os.environ['webdriver.chrome.driver'] = ChromeDriver
    driver = webdriver.Chrome(ChromeDriver)
    RunSogou(driver,sys._getframe().f_code.co_name)

def FireFox():
    if os.name == 'nt':
        FireFox = 'C:\Program Files\Mozilla Firefox'
        os.environ['path'] = FireFox # Should add firefox browser to PATH environment for additional
        # Should copy geckodriver.exe to C:\Program Files (x86)\Mozilla Firefox
        driver = webdriver.Firefox()
    elif os.name == 'posix':
        GeckoDriver = os.path.join(os.path.abspath('.'),'Drivers','geckodriver')
        os.environ['webdriver.gecko.driver'] = GeckoDriver
        driver = webdriver.Firefox(GeckoDriver)
    RunSogou(driver,sys._getframe().f_code.co_name)

def RunSogou(driver,browser):
    driver.maximize_window() #Maxmize browser
    # Open baidu website then wait for 3 seconds
    driver.get("http://www.baidu.com")
    time.sleep(3)
    # Check the title name on index of baidu
    try:
        assert '百度一下，你就知道' in driver.title
    except Exception as e:
        print(str(e))
        print("Current title name is " + driver.title)
        driver.quit()
    # Store a content then find searchbox and button on website
    SearchBox = driver.find_element_by_name("wd")
    SearchButton = driver.find_element_by_id("su")
    time.sleep(3)
    # Input the content and click search button on website
    SearchBox.send_keys(browser)
    time.sleep(3)
    SearchButton.click()
    time.sleep(3)
    # To check the titile is right
    try:
        assert browser + '_百度搜索' in driver.title
    except Exception as e:
        print(e)
        print("Current title name is " + driver.title)
        driver.quit()
    
    if browser + '_百度搜索' == driver.title: #Should add a 'u' before Chinese string
        print("Title of search page is right!")
    else:
        print("Current title name is " + driver.title)

    if browser in driver.title:
        print("Pass: " + browser)
    else:
        print("Current title name is " + driver.title)
    print("=========================================")
    time.sleep(2)
    driver.quit() # Quit the browser

if __name__ == '__main__':
    IE()
    Chrome()
    FireFox()
