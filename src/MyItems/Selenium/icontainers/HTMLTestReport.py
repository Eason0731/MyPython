import os,unittest,time,HTMLTestRunner

def HTMLTestReport():
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*Case.py') # 加载测试用例，根据文件路径 执行Demo开头的py文件
    Today = time.strftime("%Y%m%d",time.localtime())

    ReportResultDir = os.path.join('E:\\','Test Report','Selenium Test',Today)
    now = time.strftime("%Y-%m-%d %H-%M-%S") # 按照一定的格式获取当前的时间
    #filename = ReportResultDir + now + '_API_Test_Result.html' 
    if not os.path.exists(os.path.join(ReportResultDir)):
        os.makedirs(os.path.join(ReportResultDir))
        
    filename = os.path.join(ReportResultDir,now)+ '_Selenium_Test_Result.html'  # 定义报告存放路径 目前是存在运行的当前目录
    fp = open(filename, "wb") # 打开file文件流
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Selenium自动化回归测试报告',description='测试用例执行情况 by Eason') # 定义测试报告 
    runner.run(discover) # 运行测试
    
    fp.close() # 关闭报告文件
