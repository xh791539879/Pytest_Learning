class TestProduct:

    def test_product_01(self,login,product):  #调用两个方法，一个全局方法，一个自身方法，多层级嵌套实现逻辑
        print('\n这是商品管理测试用例'+product)
        print('本次测试对象为'+str(product))

    def test_product_02(self):
        print('\n这是test_product02')
