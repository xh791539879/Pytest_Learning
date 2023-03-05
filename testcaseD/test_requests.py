
"""
requests.get()
requests.post()
requests.put()
requests.delete()
requests.request()
"""
import re
import warnings
import requests

from common.yaml_util import write_yaml
from common.yaml_util import read_yaml


class TestRequest:
    sess = requests.session()

    #定义全局变量（类变量）
    # tokencode = ''

    # 忽略证书验证
    warnings.filterwarnings("ignore")

    #get，以新疆门户登录获取token为例
    def test_get_token(self):
        url = "https://ks-test.yxlearning.com/api/cms/login.gson"
        data = {
            "callback": "jQuery36009903474698827432_1677220399725",
            "account": "MTUwMzAyMjAyMzAxMjk4Nzc3",
            "password": "YWJjMTIzNDU2",
            "roleType": "4",
            "_": "1677220399728"
        }
        response = requests.get(url=url,params=data)
        # print(response.text)
        #正则表达式截取tokencode
        token = re.search(r'"tokenCode":"(.*?)","isOneLogin"',response.text)
        write_yaml({"tokencode": token.group(1)})
        # print(token.group(1))#group（）表示输入正则表达式整体，（1）输出第一个括号内
        # TestRequest.tokencode =token.group(1) #将截取道德tokencode传给全局变量

        #新疆招聘平台，获得我的报名列表信息
    def test_post_myapplicationlist(self):
        url = "https://ks-test.yxlearning.com/api/base/apply-entity/find-apply.gson"
        headers = {
            "token": read_yaml("tokencode") #调用yaml配置文件中的全局变量
        }
        response = requests.post(url=url,headers=headers)
        print(response.json())

    #更新资料接口
    def test_post_updateinfo(self):
        url = "https://ks-test.yxlearning.com/api/base/account/update-personal-info.gson"
        headers = {
            "token": read_yaml("tokencode")  #调用全局变量
        }
        data = {
            "accountExtInfoId": "1622766434819719170", "userName": "辛3", "cardNum": "150302202301298777", "gender": 1,
             "nation": "9e8fbe33-e615-498a-bef2-fecd12423b6f", "birthDay": "2023-01-29",
             "politicalStatus": "ee5f96a3-11d8-4547-803d-8fead7767bd3", "workPlace": "", "workTime": "",
             "regResidence": "0", "archivesPlace": "", "contactAddress": "大撒啊", "linePhone": "",
             "mobilePhone": "17100010014", "msgCode": "", "schoolName": "的萨达是", "schoolName1st": "测试",
             "graduationDate": "", "graduationDate1st": "", "education": "", "education1st": "", "educationType": "0",
             "degree": "", "experience": "", "reward": "",
             "headImage": "/group1/UIMG/20230207/5a6cf163-92bd-4362-b681-26da236082f5.jpg", "imageUrl": "",
             "cardImageFront": "/group1/UIMG/20230207/23653f0c-edcd-4353-b5b3-94810a8850b6.jpg",
             "cardImageFrontUrl": "", "handCard": "", "handCardUrl": "",
             "diplomaImage": "/group1/UIMG/20230207/1b063834-bd42-4c43-aed9-c7bf1bf7e716.jpg", "diplomaImageUrl": "",
             "cardImageBack": "/group1/UIMG/20230207/3736a696-63e1-4926-838f-26c9035c788f.jpg", "cardImageBackUrl": "",
             "academicCredentials": "/group1/UIMG/20230207/8b140abb-e738-4c59-ab99-e9e6a07a6980.jpg",
             "academicCredentialsUrl": "",
             "titleCertificate": "/group1/UIMG/20230207/c4c035ce-800e-485e-a7ad-6cc4cbd60dcd.jpg",
             "titleCertificateUrl": "", "postNamePostNo": "null", "audit": 0, "changeMobile": 0, "msgCodeToken": "",
             "relation": "", "applyAttachmentList": [], "remark": "", "enableUpdFlag": "true", "alternativePhone": "",
             "postCode": "", "officePhone": "", "politicalStatusJoinTime": "", "workYear": "1", "professional": "",
             "getProfessionalTime": "", "strongPoint": "多大事123", "email": "15035@pp.com", "workingSeniority": 0, "age": 0,
             "major": "", "major1st": "", "checked": "false", "accountId": "0dbd5109-e10a-427d-93c0-2286d41bc9c6",
             "applyId": "0", "cardType": 1, "unitId": "40000", "myEducationList": [], "myDegreeList": [],
             "myExperienceList": [], "myRelationList": [], "applyAttachmentJson": "[]", "myEducationStr": "[]",
             "myDegreeStr": "[]", "myExperienceStr": "[]", "myRelationStr": "[]"
        }
        response = requests.post(url=url,headers=headers,json=data)
        print(response.json())

    #查看我的订单列表
    def test_post_myorderlist(self):
        url = "https://ks-test.yxlearning.com/api/base/order-entity/find-order.gson"
        headers = {
            "token": read_yaml("tokencode")
        }
        response = requests.request(method="post",url=url,headers=headers)
        print(response.json())

    #上传文件接口示例
    def test_upload(self):
        url = "https://ks-test.yxlearning.com/file-system/tools/uploadImg.do"
        headers = {
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryGfl7uVhK8Zh7xbxu"
        }
        data = {
            "filename": r"file/01.png"
        }
        response = requests.request("post", url=url, files=data, headers=headers)
        print(response.json())

    def test_login(self):
        url = "https://ks-test.yxlearning.com/api/cms/login.gson"
        data = {
            "callback": "jQuery36009903474698827432_1677220399725",
            "account": "MTUwMzAyMjAyMzAxMjk4Nzc3",
            "password": "YWJjMTIzNDU2",
            "roleType": "4",
            "_": "1677220399728"
        }
        response = TestRequest.sess.request("get",url=url,params=data)
        print(response.text)


    #这个例子不对
    # def test_myexam(self):
    #
    #     url="https://ks-test.yxlearning.com/api/base/my-exam-entity/find-my-exam.gson"
    #     response = TestRequest.sess.request("post",url=url)
    #     print(response.json())


if __name__ == '__main__':
    TestRequest().test_get_token()
    # TestRequest().test_post_myapplicationlist()
    # TestRequest().test_post_updateinfo()
    # TestRequest().test_post_myorderlist()
    # TestRequest().test_upload()
    # TestRequest().test_login()
    # TestRequest().test_myexam()
