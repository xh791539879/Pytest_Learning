"""
数据驱动
"""
import pytest

class TestMa:
    @pytest.mark.parametrize('args', ['赵', '钱', '孙', '李'])
    def testma1(self, args):
        print(args)

    @pytest.mark.parametrize('args', [['赵', 13], ['钱', 14], ['孙', 15]])
    def testma2(self, args):
        print(args)

    @pytest.mark.parametrize('name,age', [['赵', 13], ['钱', 14], ['孙', 15]])
    def testma3(self, name,age):
        print(name,age)