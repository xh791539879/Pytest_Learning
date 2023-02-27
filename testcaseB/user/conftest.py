import pytest


@pytest.fixture(params=['123','456','789'])
def user_fixture(request):
    print('\n用户管理前置')
    yield request.param
    print('\n用户管理后置')