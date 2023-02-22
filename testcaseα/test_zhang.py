# !/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

import pytest

class TestZhang:


    def test_zhang(self):
        sleep(3)
        print("this is zhang")

if __name__ == '__main__':
        pytest.main(['-vs'])