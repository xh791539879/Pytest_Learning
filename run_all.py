import pytest

if __name__ == '__main__':  ##主函数执行测试用例，执行文件夹下的所有test_文件

        # 指定文件夹
        # pytest.main(['-vs','./testcaseα'])
        # 指定模块
        pytest.main(['-vs','./testcaseα/test_zhang.py'])

        #指定模块中的指定函数，
        # pytest.main(['-vs','./testcaseα/test_zhang.py::test_01_func'])

        # -n ,支持多线程
        # pytest.main(['-vs','./testcaseα','-n 3'])

        # --reruns=2,失败重跑
        # pytest.main(['-vs','./testcaseα/test_zhang.py','--reruns=2'])

        #-x 失败就终止运行
        # pytest.main(['-vs','./testcaseα/test_zhang.py','-x'])

        #--maxfail=2,有两个不通过就停止运行
        # pytest.main(['-vs','./testcaseα/test_zhang.py','--maxfail=2'])
        # -k un,只执行方法名中包含‘un’的用例
        # pytest.main(['-vs','./testcaseα/test_zhang.py','-k un'])










