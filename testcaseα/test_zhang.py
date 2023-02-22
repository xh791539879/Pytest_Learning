# !/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

import pytest


def test_01_func():
    print('this is 函数01')

class TestZhang:
    @pytest.mark.run(order=3)   #打标记，设置执行顺序
    def test_zhang(self):
        print("this is zhang")

    @pytest.mark.run(order=1)
    def test_03_rerun(self):
        print('失败重跑')
        assert 1 == 2
    @pytest.mark.run(order=2)
    def test_04_wang(self):
        print('this is wang')
        assert 1==2

    def test_05_sun(self):
        print('this is sun')

if __name__ == '__main__':
        pytest.main(['-vs'])