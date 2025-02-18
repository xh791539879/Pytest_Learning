﻿import os
from datetime import datetime

import pytest
from py.xml import html

from common.log_util import LogUtil
from common.yaml_util import clean_yaml

# --------------------------------------------------------------------
# 修改html报告格式，如果出现中文报错，修改html-report源码
# def pytest_configure(config):
#     # 添加接口地址与项目名称
#     config._metadata["项目名称"] = "新疆招聘测试项目"
#     config._metadata['接口地址'] = 'https://ks-test.yxlearning.com/'
#     # 删除Java_Home
#     config._metadata.pop("JAVA_HOME")


@pytest.hookimpl(optionalhook=True,tryfirst=True)
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试")])
    prefix.extend([html.p("测试人员: xinhang")])
# ------------------------------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def setup_logging(request):
    test_name =request.node.name

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_name = os.path.join(log_dir, f"{test_name}-{timestamp}.log")

    LogUtil.setup_logging(log_file_name)

    LogUtil.info(test_name,"\n"+"="*80)
    LogUtil.info(test_name,f"开始执行测试用例：{test_name}")
    LogUtil.info(test_name,"="* 80 + "\n")


    yield
    LogUtil.info(test_name, "\n" + "=" * 80)
    LogUtil.info(test_name, f"测试用例执行完毕: {test_name}")
    LogUtil.info(test_name, "=" * 80 + "\n")




#-------------------------------------------------------------------------
#session级别的方法
@pytest.fixture(scope="session",autouse=False)
def all_exe():
    print("\n在所有之前")
    yield
    print("\n在所有之后")

#class级别的方法
@pytest.fixture(scope="class",autouse=False)#autouse=True时，无需调用，符合条件的用例会自动执行
def del_exe():
    print("\nclass级别删除前置")
    yield
    print("\nclass级别删除后置")
#function级别的方法
@pytest.fixture(scope="function",name='login',autouse=False)
def login_exe():
    print("\n登录")
    yield
    print("\n退出登录")



@pytest.fixture(scope="session",autouse=False)   # 接口请求之前执行清空yaml的文件内容,autouse=True 自动执行
def clean_extract():                             #在需要执行的方法后调用此函数
    clean_yaml('extract.yaml')





