import unittest,requests,HTMLTestReport

class Guest_Sign(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://127.0.0.1:8000/api/user_sign/'

    def testaSign_With_Empty(self):
        Datas = {'eid':'','phone':''}
        r = requests.post(self.URL,Datas)
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')
        print ("parameter error")
        print ("===========================================")

    def testbSign_With_Error_Event_ID(self):
        Datas = {'eid':'987','phone':'小米7发布会'}
        r = requests.post(self.URL,Datas)
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'event id null')
        print ("Event is not exists!")
        print ("===========================================")

    def testcSign_With_Close_Event(self):
        Datas = {'eid':'7','phone':'荣耀手机'}
        r = requests.post(self.URL,Datas)
        result = r.json()
        self.assertEqual(result['status'],10023)
        self.assertEqual(result['message'],'event status is not available')
        print ("Event status is not available")
        print ("===========================================")

    def testdSign_With_Started_Event(self):
        Datas = {'eid':'1','phone':'小米7发布会'}
        r = requests.post(self.URL,Datas)
        result = r.json()
        self.assertEqual(result['status'],10024)
        self.assertEqual(result['message'],'event has started')
        print ("Event has started")
        print ("===========================================")

    def testeSing_With_Not_Exist_Phone(self):
        CanShu = {'eid':98,'phone':'1885455232545'}
        re = requests.post(self.URL,CanShu)
        rss = re.json()
        self.assertEqual(rss['status'],10025)
        self.assertEqual(rss['message'],'user phone null')
        print ("Phone number is not exist")
        print ("===========================================")

    def testfPhone_And_Event_Not_Match(self):
        CanShu = {'eid':98,'phone':'18611001100'}
        re = requests.post(self.URL,CanShu)
        rss = re.json()
        self.assertEqual(rss['status'],10026)
        self.assertEqual(rss['message'],'user did not participate in the conference')
        print ("Phone and event are not match")
        print ("===========================================")

    def testgUser_Has_Sign_In_On_A_Event(self):
        CanShu = {'eid':11,'phone':'13818581983'}
        re = requests.post(self.URL,CanShu)
        rss = re.json()
        self.assertEqual(rss['status'],10027)
        self.assertEqual(rss['message'],'user has sign in')
        print ("User has signed in this event")
        print ("===========================================")

    def testhSing_Success(self):
        #MySign = {'eid':11,'phone':'18611001107'}
        MySign = {'eid':11,'phone':'18611001105'}
        fanhui = requests.post(self.URL,MySign)
        jieguo = fanhui.json()
        self.assertEqual(jieguo['status'],10200)
        self.assertEqual(jieguo['message'],'sign success')
        print ("Sign success")
        print ("===========================================")

if __name__ == '__main__':
    HTMLTestReport.HTMLTestReport()
