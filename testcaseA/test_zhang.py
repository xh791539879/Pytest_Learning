# !/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

import pytest


def test_01_func():
    print('this is 函数01')

class TestZhang:

    age = 18  #定义一个变量

    @pytest.mark.run(order=3)   #打标记，设置执行顺序
    def test_zhang(self):
        print("this is zhang")

    @pytest.mark.user
    @pytest.mark.run(order=1)
    def test_03_rerun(self):
        print('失败重跑')
        assert 1 == 2

    @pytest.mark.skip(reason="还未完成，暂时跳过")   #无条件跳过
    @pytest.mark.run(order=2)
    def test_04_wang(self):
        print('this is wang')
        assert 1==2

    @pytest.mark.skipif(age>=18,reason='年龄大于等于18，跳过') #有条件跳过，设置变量
    @pytest.mark.smoke
    def test_05_sun(self):
        print('this is sun')
