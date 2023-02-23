"""
(2)params：参数化（支持，列表[]，元组()，字典列表[{},{},{}]，字典元组({},{},{})

"""
import pytest
#既参数化，又设定了前后置方法
@pytest.fixture(params=['张三','李四','王五'])
def my_fixture(request):
    print('\n这是前置方法，可以实现部分以及全部测试用例前置')
    yield request.param
    print('\n这是后置方法，可以实现部分以及全部测试用例后置')

class TestLan01:

    def test_lan_01(self):
        print('\n这是test_xin01')

    def test_lan_02(self,my_fixture):
        print('\n这是test_xin02')
        print('--------'+str(my_fixture))

    def test_lan_03(self):
        print('\n这是test_xin03')

class TestLan02():

    def test_lan_04(self):
        print('\n这是test_xin04')

    def test_lan_05(self):
        print('\n这是test_xin05')

if __name__ == '__main__':
    pytest.main(['-vs','test_lan.py'])