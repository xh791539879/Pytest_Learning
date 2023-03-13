import pytest


def read_yaml():
    return ['张三','李四','王五']

@pytest.fixture(scope="function",autouse=False,params=read_yaml(),ids=['user01','user02','user03'],name='user')
def user_exe(request): # 此处request为固定写法
    print("此步实际应用中为脚本")
    yield request.param # 返回获取的数据,param没有s
    print('登陆角色为: '+request.param)