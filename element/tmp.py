import pytest

class TestTmp:
    pass
def CreateTestCase(yaml_path):
    @pytest.mark.parametrize("http_request", yaml_path)
    def func(http_request):
       print(http_request)

    return func



if __name__ == "__main__":
    setattr(TestTmp, "test_func01", CreateTestCase(yaml_path="./test.yaml"))
    setattr(TestTmp, "test_func02", CreateTestCase(yaml_path="./test.yaml"))
    pytest.main([])