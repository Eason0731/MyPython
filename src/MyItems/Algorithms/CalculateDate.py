import time
import datetime
 

def Caltime(date1,date2): #计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    #%Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    #date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S") 
    #date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
    date1=time.strptime(date1,"%Y-%m-%d")
    date2=time.strptime(date2,"%Y-%m-%d")
    #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    date1=datetime.datetime(date1[0],date1[1],date1[2])
    date2=datetime.datetime(date2[0],date2[1],date2[2])
    #返回两个变量相差的值，就是相差天数
    return date2-date1


def is_date(str): #判断日期是否为合法输入，年月日的格式需要与上面对应，正确返回True，错误返回False，注意大小写。
    try:
        time.strptime(str,"%Y-%m-%d")
        return True
    except:
        return False

def Continue():
    while(1):
        IsContinue = input("Continue or Not?(Y/N)")
        if not IsContinue.strip():
            print ("Cannot input empty infos, please input again")
        else:
            print ("                                 ")
            if IsContinue.upper() == 'Y':
                Main()
            elif IsContinue.upper() == 'N':
                exit(1)
            else:
                print ("Cannot input illegal character, please input again")
   

def Main():
    #提示信息请根据实际情况更改
    print('Please input the earlier date(E.g：xxxx-xx-xx)：')
    while True:
        dt1=input()
        if is_date(dt1)==True:
            break
        else:
            print('Do not input incorrect date , please input again!')
    #print(is_date(dt1))
    print('\nPlease input the target date(E.g：xxxx-xx-xx)：')
    while True:
        dt2=input()
        if is_date(dt2)==True:
            break
        else:
            print('Do not input incorrect date , please input again!')
    print ("========================================================")
    print ("These two days are between " + str(Caltime(dt1,dt2)))
    print ("========================================================")
    Continue()

if __name__=='__main__':
    Main()
    
     
    
