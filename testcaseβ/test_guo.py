
"""
可以通过conftest.py,实现跨文件实现前后置，
但是需要和运行的用例放到同一层级。
"""


import pytest

class TestGuo01:

    def test_guo_01(self):
        print('\n这是test_guo01')

    def test_guo_02(self,my_fixture):
        print('\n这是test_guo02')
        print('------'+str(my_fixture))

    def test_guo_03(self):
        print('\n这是test_guo03')

if __name__ == '__main__':
        pytest.main(['-vs','test_guo.py'])