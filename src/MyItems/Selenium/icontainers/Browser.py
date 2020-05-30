import os
from selenium import webdriver

def Chrome():
    if os.name == 'nt':
        CDriver = os.path.join(os.path.abspath('..'),'Drivers','chromedriver.exe')
        #CDriver = 'E:\Review Center\Drivers\chromedriver.exe'

    elif os.name == 'posix':
        CDriver = os.path.join(os.path.abspath('..'),'Drivers','chromedriver')
        #CDriver = 'E:\Review Center\Drivers\chromedriver'

    os.environ['webdriver.chrome.driver'] = CDriver
    driver = webdriver.Chrome(CDriver)
    driver.maximize_window()
    return driver
