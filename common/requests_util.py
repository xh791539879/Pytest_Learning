"""
封装requests,让后续用例每一次都从这里发送请求

统一请求封装
"""

import requests
class RequsetsUtil:
    sess = requests.session()
    def send_all_request(self, **kwargs):
        res = RequsetsUtil.sess.request(**kwargs)
        print(res.text)
        return res


