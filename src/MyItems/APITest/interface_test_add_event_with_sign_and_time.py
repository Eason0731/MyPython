import unittest,requests,hashlib,HTMLTestReport
from time import time

class Add_Event_With_Sign_And_Time(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://127.0.0.1:8000/api/sec_add_event/'
        #app_key
        self.api_key = "&Guest-Bugmaster"
        #当前时间
        now_time = time()
        self.client_time = str(now_time).split('.')[0]
        #签名sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()
    
    def testaAdd_Event_By_Get(self):
        r = requests.get(self.URL,params={'eid':1}) #输入错误的请求方式
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'request error')
        print ("Request error, it should use POST!")
        print ("==================================")

    def testbAdd_Event_With_Null_Sign(self):
        Datas={'eid':1,'name':'','limit':'','address':'','start_time':'','time':'','sign':''} #传递签名格式为空,其他随意
        r = requests.post(self.URL,data=Datas)
        result = r.json()
        self.assertEqual(result['status'],10012)
        self.assertEqual(result['message'],'user sign null')
        print ("User sign null")
        print ("==================================")

    def testcAdd_Event_Time_Out(self):
        now_time = str(int(self.client_time) - 61) #在当前时间减去61秒
        Datas={'eid':1,'':'','limit':'','address':'','start_time':'','time':now_time,'sign':'abc'} #传递错误的时间格式:122344555,或者在当前时间减去61秒
        r = requests.post(self.URL,data=Datas)
        result = r.json()
        self.assertEqual(result['status'],10013)
        self.assertEqual(result['message'],'user sign timeout')
        print ("User sign timeout")
        print ("==================================")

    def testdAdd_Event_With_Error_Sign(self):
        Datas={'eid':1,'':'','limit':'','address':'','start_time':'','time':self.client_time,'sign':'abc'} #传递错误的签名格式:abc
        r = requests.post(self.URL,Datas)
        result = r.json()
        self.assertEqual(result['status'],10014)
        self.assertEqual(result['message'],'user sign error')
        print ("User sign error")
        print ("==================================")
    
    def testeAdd_Event(self):
        Datas={'eid':98,'name':'阿隆索回归F1新闻发布会','limit':5000,'address':'西班牙','start_time':'2020-12-20 17:00:00','time':self.client_time,'sign':self.sign_md5}
        r = requests.post(self.URL,data=Datas)
        result = r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'add event success')
        print ("Add event success")
        print ("==================================")

    def testeAdd_Event(self):
        Datas={'eid':98,'name':'阿隆索回归F1新闻发布会','limit':5000,'address':'西班牙','start_time':'2020-12-20 17:00:00','time':self.client_time,'sign':self.sign_md5}
        r = requests.post(self.URL,data=Datas)
        result = r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'add event success')
        print ("Add event success")
        print ("==================================")

    def testfAdd_Same_ID_Event(self):
        Datas={'eid':98,'name':'阿隆索回归F1新闻发布会','limit':5000,'address':'西班牙','start_time':'2020-12-20 17:00:00','time':self.client_time,'sign':self.sign_md5}
        r = requests.post(self.URL,data=Datas)
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'event id already exists')
        print ("Event id already exists")
        print ("==================================")

    def testgAdd_Same_Name_Event(self):
        Datas={'eid':99,'name':'阿隆索回归F1新闻发布会','limit':5000,'address':'西班牙','start_time':'2020-12-10 17:00:00','time':self.client_time,'sign':self.sign_md5}
        r = requests.post(self.URL,data=Datas)
        result = r.json()
        self.assertEqual(result['status'],10023)
        self.assertEqual(result['message'],'event name already exists')
        print ("Event name already exists")
        print ("==================================")

    def testhAdd_Event_With_Error_Time_Format(self):
        Datas = {'eid':'122','name':'giao哥演唱会','limit':80000,'address':'给老子爬','start_time':'872333','time':self.client_time,'sign':self.sign_md5}
        re = requests.post(self.URL,Datas)
        rss = re.json()
        self.assertEqual(rss['status'],10024)
        self.assertEqual(rss['message'],'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.')
        print ("Start_time format error. It must be in YYYY-MM-DD HH:MM:SS format")
        print ("==================================")
        

if __name__ == '__main__':
    HTMLTestReport.HTMLTestReport()
