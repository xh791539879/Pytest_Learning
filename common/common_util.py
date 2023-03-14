
"""
公共方法，比如用例、类的前后置。
供其他类调用。
"""

class Common_Util:
    def setup_class(self):
        print("\nsetup_class在类之前执行一次")
    def teardown_class(self):
        print("teardown_class每在类之后执行后一次")

    def setup_method(self):
        print("\nsetup_method在用例之前执行一次")
    def teardown_method(self):
        print("\nteardown_method在用例之后执行一次")