import os,time,EasonURL,requests,unittest,HTMLTestRunner,HTMLTestReport
class Demo7(unittest.TestCase):
    def testGetDemo(self):
        result = requests.get(EasonURL.URL_get)
        status = result.status_code
        content = result.text

        self.assertEqual(200,status)
        time.sleep(2)
        print ("状态码校验通过")

        Excepted = '牛仔裤女'
        self.assertIn(Excepted,content)
        time.sleep(2)
        print (content)
        print ("===================================================")

    def testPostDemo(self):
        result = requests.post(EasonURL.URL_post['请求URL'],EasonURL.URL_post['Params'])
        status = result.status_code
        content = result.content

        self.assertTrue(200,status)
        print ("状态码校验通过")

        print (content) #因为展示测试的接口没有json，所以只能输出content

if __name__ == '__main__':
    HTMLTestReport.HTMLTestReport()
