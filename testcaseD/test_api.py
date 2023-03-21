import json
import re

import pytest
import requests
import yaml
from common.requests_util import RequsetsUtil
from common.common_util import Common_Util
from common.yaml_util import read_yaml, write_yaml


# class TestApi(Common_Util):
#                                         #可以是列表嵌套列表[['李四', '张三'], ['5', '6']]
#                                         #可以是字典，也可以是元组('JQM01','JQM02','JQM03')
#                                         #可以是列表嵌套字典[{'name':'张三'},{'age':'4'}]
#     @pytest.mark.parametrize ('caseinfo',['鉴权码01','鉴权码02','鉴权码03'] )
#     def test_api_01(self,caseinfo):
#         print("获取接口鉴权码:"+str(caseinfo))  #str强转为字符串


#可以传多个值
class TestApi():
    sess = requests.session()
    @pytest.mark.parametrize('caseinfo',read_yaml('testcaseD/get_token.yaml'))
    def test_login(self,caseinfo,clean_extract):        #登录接口
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        response = RequsetsUtil().send_all_request(method=method,url=url,params=data) #通过导入common方法中的requests封装方法进行发送请求
        # response = RequsetsUtil.sess.request()
        # print(response.text)
        assert validate in response.text  #断言相应结果是够包含特定字符串
        tokenCode = re.search(r'"tokenCode":"(.*?)","isOneLogin"', response.text)
        write_yaml('/extract.yaml',{"token":(tokenCode[1])})  #注意格式,一定要这样写才可以写入正常的yaml,方便后续读取


    @pytest.mark.parametrize('caseinfo', read_yaml('testcaseD/report_list.yaml'))
    def test_report_list(self, caseinfo):      #查询接口
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = read_yaml('/extract.yaml')
        validate = caseinfo['validate']
        response = RequsetsUtil().send_all_request(method=method, url=url, headers=data)
        assert validate == response.json()['respDesc']#断言JSON特定键的值
        # print(response.json())

    @pytest.mark.parametrize('caseinfo', read_yaml('testcaseD/upload.yaml'))
    def test_upload(self,caseinfo):  ##上传接口,需要更合适的接口
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        header = caseinfo['request']['headers']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        response = RequsetsUtil().send_all_request(method=method,url=url,headers=header,files=data)
        assert validate ==response.json()['success']
        print(response.json())


