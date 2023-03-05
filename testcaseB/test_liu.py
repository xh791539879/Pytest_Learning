
"""
setup\teardown  预执行代码/后执行代码
"""

class TestLiu:

    #在所有用例之前执行一次
    def setup_class(self):
        print('\n在类执行前初始化的工作，比如创建日志对象，连接数据库，创建接口的请求对象')

    #在每个用例之前执行一次
    def setup_method(self):
        print('\n在执行用例前执行的代码')

    def test_liu_01(self):
        print('\n这是test01')

    def test_liu_02(self):
        print('\n这是test02')

    def teardown_method(self):
        print('\n在执行用例后执行的代码')

    def teardown_class(self):
        print('\n所有用例执行后执行的代码，如销毁日志对象，销毁数据库连接，销毁接口对象')


