import re
import pytest
from common.requests_util import RequsetsUtil
from common.yaml_util import read_yaml, write_yaml


class TestUser:
    @pytest.mark.parametrize('caseinfo', read_yaml('testcaseD/user/get_token.yaml'))
    def test_user(self, caseinfo, clean_extract):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        response = RequsetsUtil.sess.request(method=method, url=url, params=data)  #当调用其他类时,会执行对方类所有方法
        # print(response.text)
        assert validate in response.text  # 断言相应结果是够包含特定字符串
        tokenCode = re.search(r'"tokenCode":"(.*?)","isOneLogin"', response.text)
        write_yaml('/extract.yaml', {"token": (tokenCode[1])})  # 注意格式,一定要这样写才可以写入正常的yaml,方便后续读取
