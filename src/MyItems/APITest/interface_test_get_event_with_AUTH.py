import requests,unittest,HTMLTestReport

class get_event_with_AUTH(unittest.TestCase):
    def setUp(self):
        self.URL = 'http://127.0.0.1:8000/api/sec_get_event_list/'

    def testaAuth_Null(self):
        user_auth=('','') #user_auth用于安全验证，这里置空,格式为user_auth=('用户名','密码'),admin/admin123456
        r = requests.get(self.URL,params = {'eid':1,'name':'小米7发布会'})
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'user auth null')
        print ("User auth null")
        print ("==============================")

    def testbAuth_Fail(self):
        user_auth=('admin','12344') #user_auth用于安全验证，这里置空,格式为user_auth=('用户名','密码'),admin/admin123456
        r = requests.get(self.URL,auth=user_auth,params = {'eid':1,'name':'小米7发布会'}) #在requests中添加auth=user_auth,以验证用户是否登陆的安全性
        result = r.json()
        self.assertEqual(result['status'],10012)
        self.assertEqual(result['message'],'user auth fail')
        print ("User auth fail")
        print ("==============================")

    def testcParam_Error(self):
        user_auth=('admin','admin123456') #user_auth用于安全验证，这里置空,格式为user_auth=('用户名','密码'),admin/admin123456
        r = requests.get(self.URL,auth=user_auth,params = {'eid':''}) #在requests中添加auth=user_auth,以验证用户是否登陆的安全性
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')
        print ("Parameter error")
        print ("==============================")

    def testdEmpty_Query(self):
        user_auth=('admin','admin123456') #user_auth用于安全验证，这里置空,格式为user_auth=('用户名','密码'),admin/admin123456
        r = requests.get(self.URL,auth=user_auth,params = {'eid':995}) #在requests中添加auth=user_auth,以验证用户是否登陆的安全性
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')
        print ("Query result is empty")
        print ("==============================")

    def testeSuccess_Search(self):
        auth_user=('admin','admin123456')
        rs = requests.get(self.URL,auth=auth_user,params={'eid':11})
        result = rs.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
        print ("Search Success!")
        print (result)
        print ("==============================")

if __name__ == '__main__':
    HTMLTestReport.HTMLTestReport()
