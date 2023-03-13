"""
@pytest.fixture()装饰器实现部分用例前后置

(1)scope表示的是被@pytest.fixture标记的方法的作用域。function(默认)，class类， module模块，package/session包.
(2)params：参数化（支持，列表[]，元组()，字典列表[{},{},{}]，字典元组({},{},{})
(3)autouse=True：自动使用，默认False
(4)ids：当使用params参数化时，给每一个值设置一个变量名。意义不大。
(5)name：给表示的是被@pytest.fixture标记的方法取一个别名。当取了别名之后，那么原来的名称就用不了了
"""
import pytest

from common.common_util import Common_Util


# @pytest.fixture(scope='class',autouse=True)
# def my_fixture():
#     print('\n这是前置方法，可以实现部分以及全部测试用例前置')
#     yield
#     print('\n这是后置方法，可以实现部分以及全部测试用例后置')

class TestXin01(Common_Util): # 导入common中的工具包，引入前置后置。就不需要在每个用例类中写前置后置方法。

    def test_xin_01(self):
        print('\n这是test_xin01')

    def test_xin_02(self):
        print('\n这是test_xin02')

    def test_xin_03(self):
        print('\n这是test_xin03')

class TestXin02():

    def test_xin_04(self):
        print('\n这是test_xin04')

    def test_xin_05(self):
        print('\n这是test_xin05')
