from locust import HttpUser,TaskSet,task

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/login_action",{"username":"admin","password":"admin123456"})

    @task(2)
    def event_manage(self):
        self.client.get("/event_manage/")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage/")

    @task(2)
    def search_phone(self):
        self.client.get("/search_phone/",params={"phone":'13800112541'})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior] #从0.9版本升级到1.3，启动任务的语句变换，参考stackoveflow解决
    min_wait = 3000
    max_wait = 6000

#执行语句:locust -f Locust_Test_2.py --host=http://127.0.0.1:8888
