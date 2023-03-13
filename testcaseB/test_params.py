"""
params 实现数据驱动，
代码逻辑为：params传值给request，request将其打印

ids(次要),重新定义变量名
"""
import pytest

class TestParams:
    def test_params01(self,db):
        print('this is params01:'+db)#调用conftest中的方法，作用到单个用例上，做到用例和方法分置。
    def test_params02(self,db,add):
        print("this is params02:"+db+add)  #同时调用两个方法，可以同时作用。

@pytest.mark.usefixtures("user")  #调用conftest中的全局方法，作用到class
class TestParamss:
    def test_paramss01(self):
        print("this is paramss01")
    def test_paramss02(self):
        print("this is paramss02")