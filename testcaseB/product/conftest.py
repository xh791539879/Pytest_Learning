import pytest

def read_yaml():
    return['显示器','键盘','鼠标']
@pytest.fixture(scope="function",autouse=False,params=read_yaml(),ids=['product01','product02','product03'],name="product")
def product_exe(request):
    print("前置条件、操作")
    yield request.param
    print('\r\n'"关闭")