import pytest

#
@pytest.fixture(scope='function', autouse=False, params=['111', '222'])
def my_fixture(request):
    print('\nmy_fixture前置操作')
    yield request.param
    print('\nmy_fixture后置操作')

