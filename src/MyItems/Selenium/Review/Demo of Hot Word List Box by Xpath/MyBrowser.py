import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def IE():
    if os.name == 'nt':
        IEDriver = os.path.join(os.path.abspath('..'),'Drivers','IEDriverServer.exe')
        #IEDriver = 'D:\Eason Code Project\Python-selenium\Selenium\Drivers\IEDriverServer.exe'
        os.environ['webdriver.ie.driver'] = IEDriver
        Ser = Service(IEDriver)
        driver = webdriver.Ie(service=Ser)
        driver.maximize_window()

    else:
        print ('IE cannot be ran on non-Windows system!')

    return driver

def Firefox():
    if not os.name == 'nt':
        FFDriver = os.path.join(os.path.abspath('..'),'Drivers','geckodriver')
        #FFDriver = 'D:\Eason Code Project\Python-selenium\Selenium\Drivers\geckodriver'
        os.environ['webdriver.gecko.driver'] = FFDriver

    elif not os.name == 'posix':
        FFDriver = os.path.join(os.path.abspath('..'),'Drivers')
        #FFDriver = 'C:\Program Files\Mozilla Firefox'
        os.environ['PATH'] = FFDriver
        
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver

def Edge():
    if not 'nt' in os.name:
        print ('Edge cannot be ran on non-Windows system!')
    
    else:
        EDriver = os.path.join(os.path.abspath('..'),'Drivers','msedgedriver.exe')
        #EDriver = 'D:\Eason Code Project\Python-selenium\Selenium\Drivers\msedgedriver.exe'
        os.environ['webdriver.edge.driver'] = EDriver
        Ser = Service(EDriver)
        driver = webdriver.Edge(service=Ser)
        driver.maximize_window()

    return driver

def Chrome():
    if os.name == 'nt':
        CDriver = os.path.join(os.path.abspath('..'),'Drivers','chromedriver.exe')
        #CDriver = 'D:\Eason Code Project\Python-selenium\Selenium\Drivers\chromedriver.exe'

    elif os.name == 'posix':
        CDriver = os.path.join(os.path.abspath('..'),'Drivers','chromedriver')
        #CDriver = 'D:\Eason Code Project\Python-selenium\Selenium\Drivers\chromedriver'

    os.environ['webdriver.chrome.driver'] = CDriver
    Ser = Service(CDriver)
    driver = webdriver.Chrome(service=Ser)
    driver.maximize_window()
    return driver

    
    
