import pytest


@pytest.fixture(params=['abc','def','ghi'])
def product_fixture(request):
    print('\n商品管理前置')
    yield request.param
    print('\n商品管理后置')