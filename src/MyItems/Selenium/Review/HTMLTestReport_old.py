import os,unittest,time,HTMLTestRunner

def HTMLTestReport(CaseName):
    test_dir = './'
    #discover = unittest.defaultTestLoader.discover(test_dir, pattern='GetTitleAndURL.py') # 加载测试用例，根据文件路径 执行指定名称的py文件
    #discover = unittest.defaultTestLoader.discover(test_dir, pattern='EasonTest_*.py')# 加载测试用例，根据文件路径执行所有EasonTest_开头的py文件
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=CaseName) # 加载测试用例，通过其他测试用例文件方法传参获取文件名称
    
    Today = time.strftime("%Y%m%d")
    ReportResultDir = os.path.join('E:\\','Test Report','Selenium Test',Today)
    now = time.strftime("%Y-%m-%d %H-%M-%S") # 按照一定的格式获取当前的时间
    #filename = ReportResultDir + now + '_API_Test_Result.html' 
    if not os.path.exists(os.path.join(ReportResultDir)):
        os.makedirs(os.path.join(ReportResultDir))
        
    filename = os.path.join(ReportResultDir,now)+ '_Selenium_Test_Result.html'  # 定义报告存放路径 目前是存在运行的当前目录
    fp = open(filename, "wb") # 打开file文件流
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Selenium回归测试报告',description='测试用例执行情况 by Eason') # 定义测试报告 
    runner.run(discover) # 运行测试
    
    fp.close() # 关闭报告文件
