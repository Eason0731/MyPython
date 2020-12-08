from locust import HttpUser,TaskSet,task
from random import randint

class UserBehavior(TaskSet):
    @task
    def user_login(self):
        number = randint(1,3001)
        phone = 1380011000 + number
        str_phone = str(phone)
        self.client.post("/api/user_sign/",data={"eid":1,"phone":str_phone})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior] #从0.9版本升级到1.3，启动任务的语句变换，参考stackoveflow解决
    min_wait = 0
    max_wait = 0

#1.4版本将命令参数--no-web 更改为 --headless，将命令中指定用户并发数的参数 -c 改为 -u，即更改命令为：
#执行语句:locust -f Locust_Test_3.py --host=http://127.0.0.1:8888 --headless -u 10 -r 10 -t 3
