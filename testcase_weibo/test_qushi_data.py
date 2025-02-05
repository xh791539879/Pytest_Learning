import os

import pytest
import requests

from common.log_util import LogUtil
from common.requests_util import send_all_request
from common.yaml_util import read_yaml


class TestWeiboRequests:
    session = requests.Session()
    @pytest.mark.parametrize('case_info',read_yaml('testcase_weibo/request.yaml'))
    def test_weibo_requests(self,case_info):
        name =case_info['name']
        method=case_info['request']['method']
        url=case_info['request']['url']
        data_or_params=case_info['request']['data_or_params']
        target_category = case_info['target_category']
        expected_desc = case_info['expected_desc']

        logger_name = f"TestWeiboRequests.{name}"

        LogUtil.info(logger_name,f'测试用例：{name},开始执行')
        LogUtil.info(logger_name,f'请求方法：{method},请求地址{url},请求参数{data_or_params}）')
        try:
            if method=='post':
                response =  send_all_request(method=method,url=url,data=data_or_params)
            else:
                response = send_all_request(method=method,url=url,params=data_or_params)
            assert response.status_code==200,f'测试用例：{name}:响应状态吗码不是200，而是{response.status_code}'

            response_data = response.json()
            # target_category = '9962'
            target_entry = None
            for entry in response_data['data']:
                if entry['category']==target_category:
                    target_entry = entry
                    break

            if target_entry is None:
                assert False,f"测试用例：{name}:没找到目标分类{target_category}"

            if 'data' in target_entry and 'data' in target_entry['data'] and 'material' in target_entry['data']['data']:
                material_data = target_entry['data']['data']['material']
                LogUtil.info(logger_name,f'测试用例：{name}数据结构符合预期')
            else:
                assert False, f'测试用例：{name}：数据结构不符合预期'

            assert target_entry is not None,f'测试用例{name}:没找到9962这个字段'
            # expected_desc = "兽医师称：艾特是窒息死亡，与年纪或有没有病无关。"
            assert material_data[0]['desc']==expected_desc,f'测试用例：{name}：desc断言失败,期望值为{expected_desc},实际desc为{material_data[0]['desc']}'
            LogUtil.info(logger_name,f'测试用例：{name},执行成功')

        except AssertionError as e:
            LogUtil.error(logger_name,f'测试用例{name}，测试失败:{e}')
            pytest.fail(str(e))
        except Exception as e:
            LogUtil.error(logger_name,f'测试用例：{name}异常，{e}')
            pytest.fail(f'测试用例：{name}异常，{e}')




