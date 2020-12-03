import requests
import unittest


class get_event_list_api_test(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def testevent_null(self):
        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')
        print ("Event id is empty!")
        print ("----------------------------------------------------------")

    def testevent_is_not_exists(self):
        r = requests.get(self.url,params={'eid':'2020'})
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')
        print ("Event is not exist!")
        print ("----------------------------------------------------------")
        
    def testevent_success(self):
        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        if result['status'] == 10200:
            print ("Status Code veify success!")
        else:
            print ("actual status code is " + str(result['status']))

        if result['message'] == "success":
            print ("message veify success!")
        else:
            print ("actual message is " + str(result['message']))

        if result['data']['eid'] == 1:
            print ("eid veify success!")
        else:
            print ("actual eid is " + str(result['data']['eid']))
    
        if result['data']['name'] == '小米7发布会':
            print ("Event veify success!")
        else:
            print ("actual Event is " + str(result['data']['name']))
    
        if result['data']['limit'] == 2000:
            print ("limit veify success!")
        else:
            print ("actual limit is " + str(result['data']['limit']))

        if result['data']['status'] == True:
            print ("status veify success!")
        else:
            print ("actual status is " + str(result['data']['status']))
    
        if result['data']['address'] == "北京":
            print ("address veify success!")
        else:
            print ("actual address is " + str(result['data']['address']))

        if result['data']['start_time'] == "2018-01-30T14:00:00":
            print ("status_time veify success!")
        else:
            print ("actual status_time is " + str(result['data']['start_time']))

        """

        assert result['status'] == 10200
        assert result['message'] == "success"
        assert result['data']['eid'] == 1
        assert result['data']['name'] == '小米7发布会'
        assert result['data']['limit'] == 2000
        assert result['data']['status'] == True
        assert result['data']['address'] == "北京"
        assert result['data']['start_time'] == "2018-01-30T14:00:00"
        """

if __name__ == "__main__":
    unittest.main()
