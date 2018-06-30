import os
from DataUtil import currentDate,currentTime

#该类文件封装方法主要用于创建目录,用于存放异常截图
def createDir():
    currentPath = os.path.dirname(os.path.abspath(__file__)) #获取当前文件所在目录的绝对路径
    today = currentDate() #获取今天的日期字符串
    dateDir = os.path.join(currentPath,today) #构造以今天日期命名的目录的绝对路径
    print (dateDir)
    if not os.path.exists(dateDir): #如果文件夹不存在则创建
        os.mkdir(dateDir)

    now = currentTime() #获取当前时间的字符串
    timeDir = os.path.join(dateDir,now) #构造以今天的日期和时间的目录的绝对路径
    print (timeDir)
    if not os.path.exists(timeDir): #如果该目录不存在则创建
        os.mkdir(timeDir)
    return timeDir
