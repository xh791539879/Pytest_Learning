import re

import pytest
import requests

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
class TestApi02():
    sess = requests.session()
    @pytest.mark.parametrize('caseinfo',read_yaml('testcaseD/get_token.yaml'))
    def test_api_01(self,caseinfo):
        print("测试接收到的数据为：")
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['request']['data']

        response = TestApi02.sess.request(method=method,url=url,params=data)
        token = re.search(r'"tokenCode":"(.*?)","isOneLogin"', response.text)
        write_yaml({"tokencode": token.group(1)})
