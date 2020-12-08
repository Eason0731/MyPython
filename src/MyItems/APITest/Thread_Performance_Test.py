import requests,threading
from time import time

url = "http://127.0.0.1:8888/api/user_sign/"

#签到进程
def sign_thread(start_user,end_user):
    for i in range(start_user,end_user):
        phone = 13800110000 + i
        #phone = 1380011070
        datas = {"eid":1,"phone":phone}
        r = requests.post(url,data=datas)
        result = r.json()
        """
        try:
            assert result["message"] == "sign success"
        except Exception as e: #AssertionError
            print ("phone:" + str(phone) + ", user sign fail!")
            print (str(e))
        """
        if "sign success" in result["message"]:
            print ("phone:" + str(phone)+ " sign success!")
        else:
            print ("phone:" + str(phone) + ", user sign fail!")
            print (result["message"])

#设置用户分组(即5个线程)
lists = {1:601,601:1201,1201:1801,1801:2401,2401:3001}

#创建线程组数
threads = []

#创建线程
for start_user,end_user in lists.items():
    t = threading.Thread(target=sign_thread,args=(start_user,end_user))
    threads.append(t)


if __name__ == '__main__':
    #开始时间
    start_time = time()

    #启动线程
    for i in range(len(lists)):
        threads[i].start() #启动线程
    for i in range(len(lists)):
        threads[i].join() #守护线程

    #结束时间
    end_time = time()
    print ("start time: " + str(start_time))
    print ("end time: " + str(end_time))
    print ("run time: " + str(end_time - start_time))

#输入命令 python Thread_Performance_Test.py
