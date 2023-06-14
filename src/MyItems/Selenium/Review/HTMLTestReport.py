import os,unittest,time,HTMLTestRunner,SendMail

def HTMLTestReport(CaseName):
    test_dir = './'
    #discover = unittest.defaultTestLoader.discover(test_dir, pattern='EasonTest_*.py')# 加载测试用例，根据文件路径执行所有EasonTest_开头的py文件
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=CaseName) # 加载测试用例，通过其他测试用例文件方法传参获取文件名称
    
    Today = time.strftime("%Y%m%d")
    ReportResultDir = os.path.join('E:\\','Test Report','Selenium Test',Today)

    time.sleep(3)
    now = time.time()
    timeArray = time.localtime(now)
    
    Report_Name = time.strftime("%Y-%m-%d %H-%M-%S",timeArray) # 按照一定的格式获取当前的时间
    Execute_Time = time.strftime("%Y-%m-%d %H:%M:%S",timeArray) # 按照一定的格式获取当前的时间，并将执行时间传给邮件主题
    #filename = ReportResultDir + Execute_Time + '_API_Test_Result.html' 
    if not os.path.exists(os.path.join(ReportResultDir)):
        os.makedirs(os.path.join(ReportResultDir))
        
    filename = os.path.join(ReportResultDir,Report_Name)+ '_Selenium_Test_Result.html'  # 定义报告存放路径 目前是存在运行的当前目录
    fp = open(filename, "wb") # 打开file文件流
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Selenium回归测试报告',description='测试用例执行情况 by Eason') # 定义测试报告 
    runner.run(discover) # 运行测试
    
    fp.close() # 关闭报告文件

    New_Report(ReportResultDir,Execute_Time)

def New_Report(Test_Report_Path,Execute_Time):
    #Test_Report_Path = os.path.join('E:\\','Test Report','Selenium Test',Today)
    lists = os.listdir(Test_Report_Path) # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(Test_Report_Path + "\\" + fn)) # 按时间排序
    Latest_Report_Path = os.path.join(Test_Report_Path, lists[-1]) # 获取最新的文件保存到Latest_Report_Path
    print("最新的测试报告文件为:" + Latest_Report_Path)
    SendMail.Via_Sina(Latest_Report_Path,Execute_Time) #通过新浪邮箱发送报告
    SendMail.Via_QQ(Latest_Report_Path,Execute_Time) #通过QQ邮箱发送报告
    #SendMail.Via_Sohu(Latest_Report_Path,Execute_Time) #通过搜狐邮箱发送报告
    SendMail.Via_111Mail(Latest_Report_Path,Execute_Time) #通过111完美邮箱发送报告
    return Latest_Report_Path

"""
if __name__ == '__main__':
    HTMLTestReport() #直接在该脚本文件中运行需要执行的脚本文件，并生成测试报告到指定路径
"""
