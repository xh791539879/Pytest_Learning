"""
fixture 方法级别‘function’，使用方法
"""
import pytest


@pytest.fixture(scope="function",autouse=False)
def exe_database_sql():
    print("执行sql查询")
    yield "success"   #用yeild也同理
    print("关闭数据库")

class TestWang:
    def test_wang01(self):
        print("this is wang01")
    #单个用例手动调用fixture的方法
    def test_wang02(self,exe_database_sql):
        print("this is wang02")
        print(exe_database_sql)  #如果fixture有return或yeild,那么可以把这个值传到用例中