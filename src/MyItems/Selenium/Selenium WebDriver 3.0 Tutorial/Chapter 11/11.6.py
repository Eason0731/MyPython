import os
import unittest
from selenium import webdriver
import time


class DownloadFileAutomaticallyViaFirefox(unittest.TestCase):
    def setUp(self):
        Profile = webdriver.FirefoxProfile() #创建一个FirefoxProfile实例,用于存放自定义配置
        Profile.set_preference('browser.download.dir','D:\\FirefoxDownload') #利用.set_preference方法添加参数,'browser.download.dir'可以设置指定的下载路径
        Profile.set_preference('browser.download.folderList',2) #利用.set_preference方法添加参数,'browser.download.folderList'表示将文件下载到指定路径,0表示下载到桌面,1表示下载到默认路径,2代表使用自定义下载路径
        Profile.set_preference('browser.helperApps.alwaysAsk.force',False) #'browser.helperApps.alwaysAsk.force'对于未知的MIME类型文件会弹出窗口,让用户操作设置为True,否则设置为False
        Profile.set_preference('browser.download.manager.showWhenStarting',False) #'browser.download.manager.showWhenStarting'设置在开始下载的时候是否显示下载管理器,True为显示,False为不显示
        Profile.set_preference('browser.download.manager.useWindow',False) #'browser.download.manager.useWindow'用于显示下载框,True为显示,False为不显示
        Profile.set_preference('browser.download.manager.focusWhenStarting',False) #'browser.download.manager.focusWhenStarting'表示焦点获取,True为显示,False为不显示
        Profile.set_preference('browser.download.manager.alertOnEXEOpen',False) #'browser.download.manager.alertOnEXEOpen'表示下载exe文件弹出警告,True为显示,False为不显示
        Profile.set_preference("browser.helperApps.neverAsk.openFile","application/pdf") #"browser.helperApps.neverAsk.openFile"表示直接打开下载文件,不显示确认框;'application/pdf'表示PDF文件
        Profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,application/octec-stream') #'browser.helperApps.neverAsk.saveToDisk'表示对所给文件类型不再弹出提示框进行询问,直接保存到本地磁盘
        Profile.set_preference('browser.download.manager.showAlertOnComplete',False) #'browser.download.manager.showAlertOnComplete'表示文件下载完是否弹窗显示,True为显示,False为不显示
        Profile.set_preference('browser.download.manager.closeWhenDone',False) #'browser.download.manager.closeWhenDone'表示下载完成后是否关闭下载管理器,True为显示,False为不显示
        
        self.driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe',firefox_profile = Profile) #在'C:\Program Files\Mozilla Firefox'启动Firefox浏览器,firefox_profile是带参数启动


    def testDownloadFileAutomaticallyViaFirefox(self):
        driver = self.driver
        PythonDownloadWebSite = "https://www.python.org/downloads/release/python-365/"
        GeckoDriverDownloadWebSite = "https://github.com/mozilla/geckodriver/releases"

        driver.get(PythonDownloadWebSite)
        time.sleep(2) #等待2秒
        DownloadPythonLink = driver.find_element_by_link_text('Windows x86-64 executable installer') #找到Python3.6.5版本的x86,x64通用版exe文件下载链接地址
        DownloadPythonLink.click()
        time.sleep(50)

        driver.get(GeckoDriverDownloadWebSite)
        time.sleep(2) #等待2秒
        DownloadGeckoDriverLink = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[5]/a/strong') #找到Firefox浏览器驱动文件geckodriver的0.21版本的x86系统的exe文件下载链接地址
        DownloadGeckoDriverLink.click()
        time.sleep(50)
               
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
