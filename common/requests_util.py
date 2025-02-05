"""
封装requests,让后续用例每一次都从这里发送请求

统一请求封装
"""

import requests


def send_all_request(**kwargs):
    res = RequestsUtil.sess.request(**kwargs)
    print(res.text)
    return res


class RequestsUtil:
    sess = requests.session()


