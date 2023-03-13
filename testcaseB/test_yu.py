"""
fixture 类级别的用法，‘class’
"""
import pytest


@pytest.fixture(scope="class",autouse=False)
def exe_database_sql():
    print("进行数据库查询")
    yield
    print("关闭数据库")

class TestYu:
    def test_yu01(self):
        print("this is yu01")
    def test_yu02(self):
        print("this is yu02")

#class手动调用fixture的方法
@pytest.mark.usefixtures("exe_database_sql")
class TestYuu:
    def test_yuu01(self):
        print("this is yuu01")
    def test_yuu02(self):
        print("this is yuu02")