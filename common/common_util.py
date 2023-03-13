
"""
公共方法，比如用例、类的前后置。
供其他类调用。
"""

class Common_Util:
    def setup_class(self):
        print("每个类之前执行一次")
    def teaedown_class(self):
        print("每个类之后执行后一次")

    def setup(self):
        print("每个用例之前执行一次")
    def teardown(self):
        print("每个用例之后执行一次")