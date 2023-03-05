import pytest

from common.yaml_util import clean_yaml


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "新疆招聘"
    config._metadata['接口地址'] = 'https://ks-test.yxlearning.com/login?redirect=%2F'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.fixture(scope="function")
def exe_sql():
    print("全局,用例执行之前")
    yield
    print("全局,用例执行之后")


@pytest.fixture(scope="session",autouse=True)   # 在所有的接口请求之前执行清空yaml的文件内容,autouse=True 自动执行
def clean_extract():
    clean_yaml()