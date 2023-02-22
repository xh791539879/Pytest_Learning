from time import sleep

import pytest


class TestLi:

    def test_li(self):
        sleep(3)
        print("this is li")

if __name__ == '__main__':
        pytest.main(['-s'])