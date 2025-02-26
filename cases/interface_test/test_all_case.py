import getopt
import inspect
import logging
import os
import sys
import time
from pathlib import Path
import pytest

from commons.assert_utils import AssertUtils
from commons.yaml_utils import read_case_yaml
from commons.utils import verify_yaml, ExtractUtils
from commons.requests_utils import RequestsUtils

ru = RequestsUtils()


class TestAllCase:
    pass


def CreateTestCase(yaml_path):
    @pytest.mark.parametrize("http_request", read_case_yaml(yaml_path))
    def func(self, http_request):
        # print(http_request)
        if isinstance(http_request, list):
            for case in http_request:
                ru.start_standard_process(http_request=case)
        else:
            ru.start_standard_process(http_request=http_request)

    return func


test_case_path = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:", ["path="])
except getopt.GetoptError:
    print('-h -p --path')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('-h -p --path')
        sys.exit()
    elif opt in ("-p", "--path"):
        test_case_path = arg
# print(test_case_path)
yaml_case_list = Path(test_case_path).glob('**/*.yaml')
# print(yaml_case_list)
for yaml_case_yaml in yaml_case_list:
    # print(yaml_case_yaml.stem)
    # 通过反射 生成一个函数，把函数加入到TestAllCase下面
    setattr(TestAllCase, "test_" + yaml_case_yaml.stem, CreateTestCase(yaml_case_yaml))
