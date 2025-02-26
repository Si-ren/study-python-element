import os

import yaml


def read_testcase(yaml_path):
    test_case_path = os.walk(yaml_path).__next__()[1]
    print(test_case_path)
    yaml_case_list = test_case_path.glob('**/*.yaml')
    print(yaml_case_list)
    for yaml_case_yaml in yaml_case_list:
        print(yaml_case_yaml + yaml_case_yaml.stem)


def read_case_yaml(yaml_file):
    """
    读取yaml
    :return:
    """
    with open(yaml_file, 'r', encoding="utf-8") as f:
        case_list = yaml.safe_load(f)
        if case_list is None:  # 检查文件是否为空
            print("文件为空：空测试用例")
            return {}
        return case_list


def read_extract_yaml(yaml_file):
    with open(yaml_file, 'r', encoding="utf-8") as f:
        extract_list = yaml.safe_load(f)
        if extract_list is None:  # 检查文件是否为空
            print("没有需要抽取的值")
            return {}
        return extract_list


def write_yaml(data):
    with open("extract.yaml", encoding="utf-8", mode="a+") as f:
        yaml.safe_dump(data, f, allow_unicode=True, default_flow_style=False)
