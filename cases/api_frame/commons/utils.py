import copy
import re
from dataclasses import dataclass
from string import Template
import yaml
from commons.yaml_utils import read_case_yaml, write_yaml, read_extract_yaml

import jsonpath

from function.function import Function


@dataclass
class CaseInfo(object):
    name: str
    request: dict
    validate: dict
    retry: int = 1  # 默认重试3次
    retry_interval: int = 1  # 默认重试间隔1秒
    fail_fast: bool = False  # 失败是否立即终止
    extract: dict = None

def verify_yaml(case_info: dict):
    try:
        new_casein = CaseInfo(**case_info)
        return new_casein
    except Exception:
        raise Exception("yaml格式不符合框架规范。")

class ExtractUtils:

    @staticmethod
    def extract(resp, var_key, attr_name, expr, index):
        new_resp = copy.deepcopy(resp)
        try:
            new_resp_json = new_resp.content.json()
            # print(new_resp_json)
        except Exception:
            print("response is not json")
        data = getattr(new_resp, attr_name)
        # print("data: %s" % data)
        if expr.startswith("$"):
            l = jsonpath.jsonpath(dict(data), expr)
            print("jsonpath")
        else:
            l = re.findall(expr, str(data))
        if l:
            var_value = l[index]
            # print(var_key + '11111' + var_value)
            write_yaml({var_key: var_value})

    def use_extract_value(self, request_data: dict):
        data_dict_str = yaml.safe_dump(request_data)
        # new_request_data = Template(data_dict_str).safe_substitute(read_extract_yaml("./extract.yaml"))
        new_request_data = self.hotload_replace(data_dict_str)
        new_data_dict = yaml.safe_load(new_request_data)
        return new_data_dict

    def hotload_replace(self, data_str: str):
        # regexp = "\\$\\{(.*?)\\}"
        regexp = "\\$\\{(.*?)\\((.*?)\\)\\}"
        func_list = re.findall(regexp, data_str)
        new_value = None
        for func in func_list:
            if func[1] == "":
                new_value = getattr(Function(), func[0])()
            else:
                new_value = getattr(Function(), func[0])(*func[1].split(","))
            if isinstance(new_value, str) and new_value.isdigit():
                new_value = "'" + new_value + "'"
            old_value = "${" + func[0] + "(" + func[1] + ")"
            data_str = data_str.replace(old_value, new_value)
        return data_str
