import unittest,requests,json,HTMLTestReport,base64
from Crypto.Cipher import AES

class Get_Guest_List_With_AES(unittest.TestCase):
    def setUp(self):
        # 字符串自动补全16倍数
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

        self.URL = "http://127.0.0.1:8000/api/sec_get_guest_list/"

    def encryptBase64(self,src):
        """
        生成 base64 字符串
        """
        return base64.urlsafe_b64encode(src)

    def encryptAES(self, src):
        """
        生成AES密文
        """
        key = b'W7v4D60fds2Cmk2U'
        iv = b"1172311105789011"
        cryptor = AES.new(key, AES.MODE_CBC, iv)
        src_str = self.pad(src)
        src_byte = src_str.encode('utf-8')
        ciphertext = cryptor.encrypt(src_byte)  # AES加密
        aes_base64 = self.encryptBase64(ciphertext)  # base64 二次加密
        return aes_base64

    def testaGet_Guest_List_Request_Error(self):
        Datas = {'eid':'','phone':''}
        encoded = self.encryptAES(json.dumps(Datas)).decode() #将传参值都加密处理

        r = requests.get(self.URL,data={'data':encoded}) #用错误的请求方式Get
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'request error')
        print ("Parameter error, it should use POST!")
        print ("=====================================================")

    def testbGet_Guest_List_With_Null_Data(self):
        Datas = {'eid':'','phone':''}
        encoded = self.encryptAES(json.dumps(Datas)).decode() #将传参值都加密处理

        r = requests.post(self.URL,data={'data':encoded}) 
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'eid cannot be empty')
        print ("Event id cannot be empty")
        print ("=====================================================")

    def testcGet_Guest_List_With_Error_Eid(self):
        Datas = {'eid':133,'phone':''}
        encoded = self.encryptAES(json.dumps(Datas)).decode() #将传参值都加密处理

        r = requests.post(self.URL,data={'data':encoded}) 
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')
        print ("Query result is empty")
        print ("=====================================================")

    def testdGet_Guest_List_With_Eid_Success(self):
        Params = {'eid':11,'phone':''}
        encoded = self.encryptAES(json.dumps(Params)).decode() #加密操作

        re = requests.post(self.URL,data={'data':encoded})
        rss = re.json()
        self.assertEqual(rss['status'],200)
        self.assertEqual(rss['message'],'success')
        self.assertEqual(rss['data'][0]['realname'],'Eason') #单条件查询，需要添加data[0]，获取第一个结果
        self.assertEqual(rss['data'][0]['phone'],'13818581983')
        self.assertEqual(rss['data'][0]['email'],'Eason.Zhang0731@outlook.com')
        print ("Search success!")
        print (rss)
        print ("=====================================================")

    def testeGet_Guest_List_With_Error_Phone(self):
        Params = {'eid':11,'phone':'18851210021'}
        encoded = self.encryptAES(json.dumps(Params)).decode() #加密操作

        re = requests.post(self.URL,data={'data':encoded})
        rss = re.json()
        self.assertEqual(rss['status'],10022)
        self.assertEqual(rss['message'],'query result is empty')
        print ("Phone number error!")
        print ("=====================================================")

    def testfGet_Guest_List_Success_With_ID_And_Phone(self):
        CanShu = {'eid':1,'phone':'18611001100'}
        jiami = self.encryptAES(json.dumps(CanShu)).decode() #加密操作

        fanhui = requests.post(self.URL,data={'data':jiami})
        jieguo = fanhui.json()
        self.assertEqual(jieguo['status'],200)
        self.assertEqual(jieguo['message'],'success')
        self.assertEqual(jieguo['data']['realname'],'alan') #匹配查询，所以不需要data[0]可以去除
        self.assertEqual(jieguo['data']['phone'],'18611001100')
        self.assertEqual(jieguo['data']['email'],'alen@126.com')
        self.assertEqual(jieguo['data']['sign'],True)
        print ("Search Success!")
        print (jieguo)
        print ("=====================================================")

if __name__ == '__main__':
    HTMLTestReport.HTMLTestReport()
