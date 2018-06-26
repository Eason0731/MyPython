import os
import unittest
from selenium import webdriver
import time

import traceback #引入堆栈类
from selenium.webdriver.common.by import By #导入By类
from selenium.webdriver.support.ui import WebDriverWait #导入显式等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException #导入期望场景类
from selenium.webdriver.common.keys import Keys #引入Keys包

class KillProcessOnWindows(unittest.TestCase):
    def testKillProcessOnWindows(self):
        IEDriver = webdriver.Ie(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','IEDriverServer.exe'))) #使用相对路径找到IE浏览器驱动文件的路径，并启动
        CDriver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir,os.path.pardir,'Drivers','chromedriver.exe'))) #使用相对路径找到chromedriver浏览器驱动文件的路径，并启动
        FFDriver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe') #在'C:\Program Files\Mozilla Firefox'启动Firefox浏览器

        RetrunCode = os.system('taskkill /F /iM iexplore.exe') #使用语句taskkill /F /iM 进程名.exe 去强制结束进程
        if RetrunCode == 0:
            print ("IE浏览器的进程已经被杀掉了!")
        else:
            print ("IE浏览器的进程没有被杀掉了!")

        RetrunCode = os.system('taskkill /F /iM chrome.exe') #使用语句taskkill /F /iM 进程名.exe 去强制结束进程
        if RetrunCode == 0:
            print ("Chrome浏览器的进程已经被杀掉了!")
        else:
            print ("Chrome浏览器的进程没有被杀掉了!")

        RetrunCode = os.system('taskkill /F /iM firefox.exe') #使用语句taskkill /F /iM 进程名.exe 去强制结束进程
        if RetrunCode == 0:
            print ("Firefox浏览器的进程已经被杀掉了!")
        else:
            print ("Firefox浏览器的进程没有被杀掉了!")

if __name__ == '__main__':
    unittest.main()
