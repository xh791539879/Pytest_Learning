class TestUser:

    def test_user_01(self,my_fixture,user_fixture):  #即可以调用同层级的conftest，也可以调用上一级,全局放在前
        print('\n这是test_user01')
        print('--------'+str(user_fixture))
        print('--------'+str(my_fixture))


    def test_user_02(self):
        print('\n这是test_usern02')
