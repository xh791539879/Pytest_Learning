import pytest


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "新疆招聘"
    config._metadata['接口地址'] = 'https://ks-test.yxlearning.com/login?redirect=%2F'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: xx测试中心")])
    prefix.extend([html.p("测试人员: Linux超")])