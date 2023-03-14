"""
在类TestXin01中，分别调用了common包中的setup-teardown方法和conftest中的fixture（session、class、function）
执行过程： session级别的fixture最先执行
        同级别的fixture和setup-teardown，fixture先执行
"""

from common.common_util import Common_Util

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
