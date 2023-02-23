
"""
requests.get()
requests.post()
requests.put()
requests.delete()
requests.request()
"""
import requests
class TestRequest:
    #get
    def test_get_token(self):
        url = "https://ks-test.yxlearning.com/api/cms/login.gson"
        param = {
            "callback":"jQuery360042961185183372064_1677160058590",
            "account":"MTIwMTAxMjAyMzAyMDc2Nzk0",
            "password":"YWJjMTIzNDU2",
            "roleType":"4",
            "_":"1677160058593"
        }
        response = requests.get(url=url,params=param,verify=False)
        print(response.text)
if __name__ == '__main__':
    TestRequest().test_get_token()
