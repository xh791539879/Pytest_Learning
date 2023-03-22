from http.client import responses

import pytest
import requests

from common.requests_util import RequsetsUtil
from common.yaml_util import read_yaml


class TestWeiboRequests:
    session = requests.Session()
    @pytest.mark.parametrize('case_info',read_yaml('weibo/request.yaml'))
    def test_weibo_requests(self,case_info):
        name =case_info['name']
        method=case_info['request']['method']
        url=case_info['request']['url']
        data=case_info['request']['data']
        if method=='post':
            responses =  RequsetsUtil().send_all_request(method=method,url=url,data=data)
        else:
            responses = RequsetsUtil().send_all_request(method=method,url=url,params=data)
        # response = RequsetsUtil().send_all_request(method=method,url=url,params=data)
            assert responses.status_code==200
            print(name)



        # if 'code' in response.text:
        #     code = case_info['validata']
        #     print(code)
        #     assert code == 200
        # else:
        #     print('用力异常')



