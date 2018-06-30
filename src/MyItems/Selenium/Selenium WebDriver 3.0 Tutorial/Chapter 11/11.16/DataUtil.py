import time
from datetime import datetime

#该类文件封装方法主要获取当前的日期和时间,用于生成保存截图文件目录名

def currentDate(): #构造今天的日期字符串
    date = time.localtime()
    today = str(date.tm_year) + "-" + str(date.tm_mon) + "-" +str(date.tm_mday)
    return today

def currentTime(): #构造当前时间的字符串
    timeStr = datetime.now()
    now = timeStr.strftime("%H-%M-%S")
    return now

if __name__ == '__main__':
    print (currentDate())
    print (currentTime())
