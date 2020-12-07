import unittest,requests,HTMLTestReport

class Add_Event_Test(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/add_event/'

    def testaAdd_Empty_Event(self):
        Add_Event = params={'eid': '', 'name': '', 'limit': '', 'status': '', 'address': '', 'start_time': ''}
        r = requests.post(self.url,Add_Event)
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')
        print ("Cannot add empty event!")
        print ("==============================================")

    def testbAdd_Same_ID_Event(self):
        Add_Event = params={'eid': 11, 'name': 'F1萨基尔大奖赛周四新闻发布会', 'limit': 20, 'status': 1, 'address': '巴林萨基尔赛道', 'start_time': '2020-12-23 15:00:00'}
        r = requests.post(self.url,Add_Event)
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'event id already exists')
        print ("Cannot add same id event!")
        print ("==============================================")

    def testcAdd_Same_Name_Event(self):
        Add_Event = params={'eid': 121,'name': 'F1萨基尔大奖赛周四新闻发布会', 'limit': 20, 'status': 1, 'address': '巴林萨基尔赛道', 'start_time': '2020-12-23 15:00:00'}
        r = requests.post(self.url,Add_Event)
        result = r.json()
        self.assertEqual(result['status'],10023)
        self.assertEqual(result['message'],'event name already exists')
        print ("Cannot add same name event!")
        print ("==============================================")

    def testdError_Time_Format_Event(self):
        Add_Event = params={'eid': 121,'name': 'F1萨基尔大奖赛周四新闻发布会123', 'limit': 20, 'status': 1, 'address': '巴林萨基尔赛道', 'start_time': "2017"}
        r = requests.post(self.url,Add_Event)
        result = r.json()
        self.assertEqual(result['status'],10024)
        self.assertIn('start_time format error.',result['message'])
        print ("Time format error!")
        print ("==============================================")

    def testeAdd_Event(self):
        Add_Event = params={'eid': 27,'name': '上港上港VS全北现代赛前新闻发布会', 'limit': 20, 'status': 1, 'address': '卡塔尔多哈卡莉法体育场', 'start_time': '2020-12-23 22:00:00'}
        r = requests.post(self.url,Add_Event)
        result = r.json()
        self.assertEqual(result['status'],10200)
        self.assertEqual(result['message'],'add event success')
        print ("Add event success!")
        print ("==============================================")

    

if __name__ == '__main__':
    HTMLTestReport.HTMLTestReport()
