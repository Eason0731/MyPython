from locust import HttpUser,TaskSet,task

class UserBehavior(TaskSet):
    
    @task
    def baidu_page(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior] #从0.9版本升级到1.3，启动任务的语句变换，参考stackoveflow解决
    min_wait = 3000
    max_wait = 6000
"""
from locust import HttpUser, TaskSet, task

# 定义用户行为类
class UserBehavior(TaskSet):
    @task  # 任务项
    def test_login(self):
        user_info = {
            'username':'****',
            'password':'*****'
        }
        url = 'https://smart.mail.163.com/login.htm'
        res = self.client.get(url,data = user_info)
        if res.status_code == 200:
            print('登陆成功！')
        else:
            print('登陆失败！')
            
class WebSiteUser(HttpUser):
    task_create = UserBehavior
    max_wait = 5000
"""
#启动命令locust -f Locust_Test.py --host=https://www.baidu.com
